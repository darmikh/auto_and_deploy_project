import os
from dotenv import load_dotenv
import csv
import re
import psycopg2
from pathlib import Path

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

def load_csv_to_db():
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id SERIAL PRIMARY KEY,
            doc_id VARCHAR(20),
            item VARCHAR(100),
            category VARCHAR(50),
            amount INTEGER,
            price NUMERIC(10,2),
            discount NUMERIC(10,2),
            filename VARCHAR(50),
            load_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    data_folder = Path('data')
    if not data_folder.exists():
        print("Папка data не найдена!")
        return
    
    csv_files = list(data_folder.glob('*.csv'))
    total_rows = 0
    
    for csv_file in csv_files:
        if not re.match(r'\d+_\d+\.csv', csv_file.name):
            print(f"Пропускаем файл: {csv_file.name}")
            continue
        
        print(f"Загружаем {csv_file.name}...")
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows_loaded = 0
            
            for row in reader:
                cursor.execute("""
                    INSERT INTO sales (doc_id, item, category, amount, price, discount, filename)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    row['doc_id'],
                    row['item'],
                    row['category'],
                    int(row['amount']),
                    float(row['price']),
                    float(row['discount']),
                    csv_file.name
                ))
                rows_loaded += 1
            
            total_rows += rows_loaded
            print(f"  Загружено строк: {rows_loaded}")
    
    conn.commit()
    print(f"\nВсего загружено записей: {total_rows}")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    load_csv_to_db()
