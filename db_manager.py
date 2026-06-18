import sqlite3
import os
from logger_setup import logger

DATABASE_FILE = 'data/storage.db'

def connect_to_storage():
    return sqlite3.connect(DATABASE_FILE)

def setup_database():
    if not os.path.exists('data'):
        os.makedirs('data')
        
    connection = connect_to_storage()
    cursor = connection.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            address TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            order_date TEXT NOT NULL,
            status TEXT CHECK(status IN ('новый','в доставке','выполнен','отменён')),
            total REAL NOT NULL,
            FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE RESTRICT
        )
    ''')
    
    connection.commit()
    connection.close()
    logger.info("База данных успешно инициализирована.")

def insert_new_customer(c_name, c_phone, c_address):
    connection = connect_to_storage()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO customers (name, phone, address) VALUES (?, ?, ?)', (c_name, c_phone, c_address))
    connection.commit()
    connection.close()
    logger.info(f"Зарегистрирован клиент: {c_name}")

def fetch_all_orders():
    connection = connect_to_storage()
    cursor = connection.cursor()
    cursor.execute('''
        SELECT o.id, c.name, o.order_date, o.status, o.total 
        FROM orders o
        INNER JOIN customers c ON o.customer_id = c.id
    ''')
    dataset = cursor.fetchall()
    connection.close()
    return dataset

def insert_new_order(c_id, o_date, o_status, o_total):
    connection = connect_to_storage()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO orders (customer_id, order_date, status, total) VALUES (?, ?, ?, ?)', 
                   (c_id, o_date, o_status, o_total))
    connection.commit()
    connection.close()
    logger.info("Запись о заказе успешно создана.")

def calculate_status_stats():
    connection = connect_to_storage()
    cursor = connection.cursor()
    cursor.execute('SELECT status, COUNT(id) FROM orders GROUP BY status')
    statistics = cursor.fetchall()
    connection.close()
    return statistics
