import csv
import random
import os

def generate_csv_files(num_shops=3, max_cash_per_shop=2):
    """Генерирует CSV-файлы для магазинов и касс"""
    
    os.makedirs('data', exist_ok=True)
    
    categories = ['бытовая химия', 'текстиль', 'посуда', 'хозтовары', 'продукты']
    items = {
        'бытовая химия': ['Порошок', 'Мыло', 'Шампунь', 'Гель для душа'],
        'текстиль': ['Полотенце', 'Простыня', 'Подушка', 'Одеяло'],
        'посуда': ['Тарелка', 'Кружка', 'Кастрюля', 'Сковорода'],
        'хозтовары': ['Ведро', 'Швабра', 'Губки', 'Пакеты'],
        'продукты': ['Чай', 'Кофе', 'Сахар', 'Печенье']
    }
    
    for shop_num in range(1, num_shops + 1):
        num_cash = random.randint(1, max_cash_per_shop)
        
        for cash_num in range(1, num_cash + 1):
            filename = f"data/{shop_num}_{cash_num}.csv"
            
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['doc_id', 'item', 'category', 'amount', 'price', 'discount'])
                
                for _ in range(random.randint(20, 50)):
                    doc_id = f"CHK{random.randint(1000, 9999)}"
                    category = random.choice(categories)
                    item = random.choice(items[category])
                    amount = random.randint(1, 5)
                    price = random.randint(50, 1000)
                    discount = random.choices([0, 5, 10, 15, 20, 30], weights=[70, 10, 8, 5, 4, 3])[0]
                    
                    writer.writerow([doc_id, item, category, amount, price, discount])
            
            print(f"Создан файл: {filename}")
    

if __name__ == "__main__":
    generate_csv_files()
