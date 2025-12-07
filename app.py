import sqlite3
from datetime import datetime
from flask import Flask, render_template

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

    # Show the educational landing page
    return render_template('landing.html')

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

    conn.close()

    return render_template('results.html', results=results)

@app.route('/preview-email')
def preview_email():
    """Preview what the phishing email looks like"""
    # Create a sample tracking URL
    sample_url = "http://localhost:5000/track/sample-token-preview"

    return render_template('phishing_email.html', tracking_url=sample_url)

@app.route('/debug-db')
def debug_database():
    """Debug route to see what's in the database"""
    conn = get_db()

    # Check all users
    users = conn.execute('SELECT * FROM users').fetchall()

    # Check all clicks
    clicks = conn.execute('SELECT * FROM clicks').fetchall()

    output = "<h2>Users Table:</h2><pre>"
    for user in users:
        output += f"{dict(user)}\n"

    output += "</pre><h2>Clicks Table:</h2><pre>"
    for click in clicks:
        output += f"{dict(click)}\n"

    output += "</pre>"
    conn.close()
    return output

if __name__ == '__main__':
    app.run(debug=True)
