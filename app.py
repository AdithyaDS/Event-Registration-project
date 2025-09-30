from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'registrations.db')

app = Flask(__name__)
# IMPORTANT: The secret key is essential for sessions (login/logout) and flash messages
app.secret_key = "replace_this_with_a_random_secret"  # CHANGE THIS!

# --- ADMIN CONFIGURATION ---
ADMIN_USERNAME = "22049"
ADMIN_PASSWORD = "12345" # <<< CHANGE THIS TO A SECURE PASSWORD
# ---------------------------

def init_db():
    """Initializes the database table if it does not exist."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Note: No 'UNIQUE' constraint is set on email, allowing duplicates if validation is weak.
    c.execute('''
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            event_type TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

# --- PUBLIC ROUTES ---

@app.route('/')
def home():
    """Renders the home page (index.html)."""
    # Pass datetime for the footer year in index.html
    return render_template('index.html', now=datetime.now)

@app.route('/register')
def register():
    """Renders the registration form page (register.html)."""
    return render_template('register.html')

@app.route('/submit', methods=['POST'])
def submit():
    """Handles form submission and saves data to the database."""
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    phone = request.form.get('phone', '').strip()
    event_type = request.form.get('event_type', '').strip()

    # Basic server-side validation
    errors = []
    if not name:
        errors.append("Name is required.")
    if not email or '@' not in email:
        errors.append("Valid email is required.")
    if phone and (not phone.isdigit() or len(phone) not in (10, 11, 12)):
        errors.append("Phone must be digits only (10-12 digits).")
    if not event_type:
        errors.append("Please select an event type.")

    if errors:
        for e in errors:
            flash(e, 'danger')
        return redirect(url_for('register'))

    # Store in sqlite
    timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute('''
            INSERT INTO registrations (name, email, phone, event_type, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, email, phone, event_type, timestamp))
        conn.commit()
        reg_id = c.lastrowid
        conn.close()

        # Data dictionary to pass to the success page
        data = {
            'id': reg_id,
            'name': name,
            'email': email,
            'phone': phone,
            'event_type': event_type,
            'timestamp': timestamp
        }
        return render_template('success.html', data=data)
    except Exception as e:
        flash(f"An unexpected error occurred during registration: {e}", 'danger')
        conn.close()
        return redirect(url_for('register'))

# --- ADMIN LOGIN/LOGOUT ---

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """Handles the admin login form submission and session management."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            flash('Logged in successfully!', 'success')
            return redirect(url_for('admin_regs'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
            return render_template('admin_login.html')

    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    """Logs the admin out by removing the 'logged_in' key from the session."""
    session.pop('logged_in', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

# --- PROTECTED ADMIN VIEW ---

@app.route('/admin/registrations')
def admin_regs():
    """Renders the protected admin view page (admin.html) with all registrations."""
    # SECURITY CHECK: Redirects non-logged-in users to the login page
    if not session.get('logged_in'):
        flash('Please log in to view the admin page.', 'warning')
        return redirect(url_for('admin_login'))

    conn = sqlite3.connect(DB_PATH)
    # Allows accessing columns by index (r[0], r[1], etc.) which matches admin.html
    c = conn.cursor()
    c.execute('SELECT id, name, email, phone, event_type, timestamp FROM registrations ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    
    return render_template('admin.html', regs=rows)

# --- APPLICATION START ---

if __name__ == '__main__':
    # FIX for deprecated @app.before_first_request: 
    # Initialize the database here, once, before starting the server.
    init_db()
    
    app.run(debug=True)