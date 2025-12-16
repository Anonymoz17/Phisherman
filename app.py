import sqlite3
from datetime import datetime
from flask import Flask, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid
import sys

# Database configuration
DATABASE = 'database.db'

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'luiztayza2035@gmail.com'
SENDER_PASSWORD = 'srsw bugd zikt prif'

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

def generate_token():
    return str(uuid.uuid4())

def send_email(recipient_email, recipient_name, tracking_url):
    """Send phishing simulation email to a recipient"""

    # Create the email message
    message = MIMEMultipart('alternative')
    message['Subject'] = 'Password Expiration Notice'
    message['From'] = SENDER_EMAIL
    message['To'] = recipient_email

    # Load and render the HTML template with the tracking URL
    with open('templates/phishing_email.html', 'r') as f:
        html_content = f.read()

    # Replace the tracking_url placeholder in the HTML
    html_content = html_content.replace('{{ tracking_url }}', tracking_url)

    # Attach HTML content to the message
    html_part = MIMEText(html_content, 'html')
    message.attach(html_part)

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(message)
    server.quit()

    print(f"Email sent to {recipient_email}")

def send_campaign():
    conn = get_db()
    users = conn.execute('''SELECT * FROM users''').fetchall()

    if not users:
        print("No users in database. Add users first!")
        conn.close()
        return

    print(f"Starting campaign for {len(users)} users...")

    for user in users:
        # Generate a UNIQUE token for THIS user
        token = generate_token()

        # Insert the token into clicks table
        conn.execute('INSERT INTO clicks (user_id, tracking_token, clicked) VALUES (?, ?, 0)', (user['id'], token))

        # Build the tracking URL
        tracking_url = f'http://localhost:5000/track/{token}'

        # Send the email
        send_email(user['email'], user['name'], tracking_url)
        print(f"Email has been sent to {user['email']}!")

    conn.commit()
    conn.close()

    print(f"\n Campaign complete! Send {len(users)} emails.")

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

@app.route('/send-test-email')
def send_test_email():
    """Send a test phishing email to yourself"""

    # 1. Create or get a test user
    conn = get_db()

    # For testing, we'll use your email - CHANGE THIS to your actual email!
    test_email = 'luiztayza2035@gmail.com' 
    test_name = 'Test User'

    # Check if user already exists
    existing_user = conn.execute('SELECT * FROM users WHERE email = ?', (test_email,)).fetchone()

    if existing_user:
        user_id = existing_user['id']
    else:
        # Insert new test user
        conn.execute('INSERT INTO users (email, name) VALUES (?, ?)', (test_email, test_name))
        user_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]
        conn.commit()

    # 2. Generate a unique tracking token
    token = generate_token()

    # 3. Save the tracking token to the database
    conn.execute('INSERT INTO clicks (user_id, tracking_token, clicked) VALUES (?, ?, 0)',
                 (user_id, token))
    conn.commit()
    conn.close()

    # 4. Build the tracking URL
    tracking_url = f'http://localhost:5000/track/{token}'

    # 5. Send the email!
    try:
        send_email(test_email, test_name, tracking_url)
        return f'''
            <h2>✅ Test Email Sent!</h2>
            <p>Check your inbox at <strong>{test_email}</strong></p>
            <p>Tracking URL: <a href="{tracking_url}">{tracking_url}</a></p>
            <p><a href="/results">View Results</a> | <a href="/debug-db">Debug Database</a></p>
        '''
    except Exception as e:
        return f'''
            <h2>❌ Error Sending Email</h2>
            <p>Error: {str(e)}</p>
            <p>Make sure you've updated your Gmail credentials in app.py!</p>
        '''

if __name__ == '__main__':
    # Check if user provided a command-line argument
    if len(sys.argv) > 1 and sys.argv[1] == 'send-campaign':
        # User ran: python app.py send-campaign
        print("🚀 Starting phishing campaign...\n")
        send_campaign()
    else:
        # User ran: python app.py (no arguments)
        # Start the Flask web server
        app.run(debug=True)
