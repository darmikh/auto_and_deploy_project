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
);
