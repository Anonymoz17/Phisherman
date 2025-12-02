import sqlite3
from flask import Flask

# Database configuration
DATABASE = 'database.db'

def get_db():
    """Connect to the SQLite database and return the connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # This lets us access columns by name
    return conn

def init_db():
    """Initialize the database by creating tables if they don't exist"""
    conn = get_db()

    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            name TEXT NOT NULL
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS clicks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            tracking_token TEXT UNIQUE NOT NULL,
            clicked BOOLEAN DEFAULT 0,
            click_timestamp DATETIME,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized successfully!")

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/init-db')
def initialize_database():
    """Route to manually initialize the database"""
    init_db()
    return "Database initialized! Check your project folder for database.db"

if __name__ == '__main__':
    app.run(debug=True)