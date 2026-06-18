import sqlite3
import pytest
import db_manager

def test_storage_initialization():
    db_manager.setup_database()
    conn = sqlite3.connect(db_manager.DATABASE_FILE)
    curr = conn.cursor()
    curr.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
    table_exists = curr.fetchone()
    conn.close()
    assert table_exists is not None

def test_customer_insertion():
    db_manager.setup_database()
    db_manager.insert_new_customer("Проверка", "000", "Где-то")
    conn = sqlite3.connect(db_manager.DATABASE_FILE)
    curr = conn.cursor()
    curr.execute("SELECT id FROM customers WHERE name='Проверка'")
    record = curr.fetchone()
    conn.close()
    assert record is not None
