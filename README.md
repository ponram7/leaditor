# Lead Generation App (Leaditor)

Leaditor is a web-based application designed for managing leads, primarily for businesses that generate and track potential customer information. Built using Django & bootstrap, the app offers an interactive and dynamic experience for users to manage their lead data.

## Features

- **Lead Management**: Create, view, and update lead information (e.g., name, email, phone, company, and status).
- **Responsive Design**: Using bootstrap ensures the app is fully responsive and provides a modern user interface.
- **Admin Interface**: Easily manage leads via the built-in Django admin panel.
- **SQLite Database**: Uses SQLite for easy local development and testing.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: bootstrap
- **Database**: SQLite (can be switched to PostgreSQL or MySQL)
- **Development Tools**: Python, pip, virtualenv

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- virtualenv (for creating isolated environments)

### Steps to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/leaditor.git
   cd leaditor
Set up a virtual environment (optional but recommended):

```bash
# Set up a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install the dependencies
pip install -r requirements.txt

# Make migrations to create the database schema
python manage.py makemigrations
python manage.py migrate

# Create a superuser to access the Django admin panel
python manage.py createsuperuser

# Run the development server
python manage.py runserver

# Access the app
# Open your browser and navigate to:
http://127.0.0.1:8000/

# The Django admin panel is available at:
http://127.0.0.1:8000/admin/


Structure
```bash
leeditor/
├── manage.py                # Django project management script
├── leaditor/                # Main Django project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py
├── leads/                   # Django app for managing leads
│   ├── __init__.py
│   ├── admin.py             # Register models for admin interface
│   ├── apps.py
│   ├── forms.py             # Forms for handling lead data
│   ├── models.py            # Database models
│   ├── tests.py             # Unit tests for leads app
│   ├── urls.py              # URL routing for leads app
│   ├── views.py             # Views for handling lead actions
│   ├── templates/           # HTML templates
│   │   └── leads/           # Templates specific to the leads app
│   ├── migrations/          # Database migrations
├── db.sqlite3               # SQLite database file (can be replaced with PostgreSQL or MySQL)
└── venv/                    # Virtual environment (not committed to version control)

