import sqlite3
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
DATABASE_FILE = os.path.join(DATA_DIR, 'exclusions.db')

def init_db():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS exclusions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            gender TEXT,
            street TEXT,
            city TEXT,
            state TEXT,
            zip TEXT,
            reason TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT,
            exclusion_authority TEXT,
            notes TEXT,
            id_type TEXT,
            id_number TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_exclusion(data):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO exclusions (
            name, date_of_birth, gender, street, city, state, zip, reason, start_date, end_date, 
            exclusion_authority, notes, id_type, id_number
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['name'], data['date_of_birth'], data['gender'], data['street'], data['city'], data['state'],
        data['zip'], data['reason'], data['start_date'], data['end_date'], data['exclusion_authority'],
        data['notes'], data['id_type'], data['id_number']
    ))
    conn.commit()
    conn.close()

def get_exclusion_by_id_number(id_number):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('SELECT * FROM exclusions WHERE id_number = ?', (id_number,))
    exclusion = c.fetchone()
    conn.close()
    return exclusion

def view_exclusions():
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('SELECT * FROM exclusions')
    exclusions = c.fetchall()
    conn.close()
    return exclusions
