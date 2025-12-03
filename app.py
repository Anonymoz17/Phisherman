import sqlite3
from datetime import datetime
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

@app.route('/create-test-data')
def create_test_data():
    """Create test user and tracking token for testing"""
    conn = get_db()

    # Insert test user
    conn.execute('''
        INSERT INTO users (email, name)
        VALUES ('test@example.com', 'Test User')
    ''')

    # Get the user ID we just created
    user_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]

    # Create a tracking token for this user
    test_token = 'test-token-123'
    conn.execute('''
        INSERT INTO clicks (user_id, tracking_token, clicked)
        VALUES (?, ?, 0)
    ''', (user_id, test_token))

    conn.commit()
    conn.close()

    return f'Test data created! Try clicking: <a href="/track/{test_token}">Track Link</a>'

@app.route('/track/<token>')
def track_click(token):
    """Log when a user clicks the tracking link"""
    # Get database connection
    conn = get_db()

    # Get current timestamp
    current_time = datetime.now()

    # Update the database to log the click
    conn.execute('''
        UPDATE clicks
        SET clicked = 1, click_timestamp = ?
        WHERE tracking_token = ?
    ''', (current_time, token))

    # Save changes to database
    conn.commit()
    conn.close()

    return f"Click tracked! Token: {token}"

@app.route('/results')
def show_results():
    """Display all clicks with user information"""
    # Get database connection
    conn = get_db()

    results = conn.execute('''
        SELECT users.email, users.name, clicks.click_timestamp
        FROM clicks
        INNER JOIN users ON clicks.user_id = users.id
        WHERE clicks.clicked = 1
    ''').fetchall()

    # Build a simple text response
    output = "<pre>=== Phishing Campaign Results ===\n\n"

    for result in results:
        output += f"Name: {result['name']}\n"
        output += f"Email: {result['email']}\n"
        output += f"Clicked at: {result['click_timestamp']}\n\n"
    output += "</pre>"

    conn.close()
    return output

if __name__ == '__main__':
    app.run(debug=True)