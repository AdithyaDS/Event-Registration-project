
# Event Registration System

A simple, self-contained web application built with Python (Flask) and SQLite for managing event registrations. It provides a public-facing registration form and a password-protected admin area to view all submitted entries.

This project is designed to be a straightforward example of a CRUD (Create, Read) application using Flask, demonstrating routing, template rendering, form handling, database interaction, and basic session-based authentication.

## ✨ Features

  * **User-friendly Registration:** A clean form for users to register for different events.
  * **Admin Panel:** A secure, password-protected dashboard for administrators.
  * **View Registrations:** Admins can view all submitted registrations in a neatly organized table, sorted with the most recent entries first.
  * **Data Persistence:** Uses a local SQLite database to store registration data, making it easy to set up without a separate database server.
  * **User Feedback:** Implements flash messages to provide clear feedback for actions like successful logins, logouts, or errors.
  * **Server-Side Validation:** Basic checks are in place to ensure submitted data is valid.

## 🛠️ Technology Stack

  * **Backend:** Python 3, Flask
  * **Database:** SQLite 3
  * **Frontend:** HTML5, Bootstrap 5

## 📂 Project Structure

The project follows a standard Flask application structure.

```
/flask-event-registration
├── app.py                  # Main Flask application file
├── registrations.db        # SQLite database file (created on first run)
├── templates/
│   ├── index.html          # Home page
│   ├── register.html       # Registration form page
│   ├── success.html        # Registration confirmation page
│   ├── admin.html          # Admin dashboard (shows registrations)
│   └── admin_login.html    # Admin login page
└── README.md               # This file
```

## 🚀 Setup and Installation

Follow these steps to get the application running on your local machine.

### 1\. Prerequisites

Ensure you have **Python 3** installed on your system.

### 2\. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/flask-event-registration.git
cd flask-event-registration
```

### 3\. Create a Virtual Environment (Recommended)

It's good practice to create a virtual environment to manage project dependencies.

  * **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
  * **On Windows:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

### 4\. Install Dependencies

The only external dependency is Flask. Install it using pip:

```bash
pip install Flask
```

### 5\. Configure the Application (Important\!)

Before running the app, you **must** change the default security settings in `app.py`.

Open `app.py` in your code editor and modify these lines:

```python
# Change the default secret key to a long, random string
app.secret_key = "your-very-strong-and-random-secret-key"

# Change the default admin password to something secure
ADMIN_PASSWORD = "YourNewSecurePassword"
```

### 6\. Run the Application

Execute the main Python script:

```bash
python app.py
```

The application will start, and the database file (`registrations.db`) will be created automatically. You can access the website by opening your web browser and navigating to:

**[http://127.0.0.1:5000](https://www.google.com/search?q=http://127.0.0.1:5000)**

## 📝 How to Use

### Public User

1.  Navigate to the homepage at `http://127.0.0.1:5000/`.
2.  Click the **"Register Now"** button.
3.  Fill in the form with your details and select an event.
4.  Click **"Submit Registration"**. You'll be redirected to a success page confirming your details.

### Administrator

1.  Navigate to the admin login page at `http://127.0.0.1:5000/admin/login`.
2.  Enter the admin credentials you configured in `app.py`:
      * **Username:** `22049`
      * **Password:** *****
3.  Upon successful login, you will be taken to the admin dashboard, which displays a table of all user registrations.
4.  To log out, click the **"Logout"** button.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
