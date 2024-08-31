# HealthCareSystem

HealthCare System
This is a Django-based healthcare management system designed to assist doctors in managing client appointments, sending automated messages via email (including birthday wishes, Christmas greetings, New Year greetings, and appointment reminders), and handling other client-related tasks efficiently.

Features
Client Management: Add, edit, and view client information.
Appointment Scheduling: Manage client appointments with ease.
Automated Messaging: Send automated emails to clients for birthdays, holidays, and appointment reminders using Celery and Redis.
Task Queue Management: Background task processing for sending emails and other time-consuming operations.
Requirements
Python 3.10+
Django 4.2.3
PostgreSQL (for database management)
Celery 5.4.0 (for task management)
Redis 4.5.1 (as a message broker for Celery)
psycopg2 2.9.6 (PostgreSQL database adapter)
Installation
1. Clone the repository
bash
Copy code
git clone https://github.com/yourusername/healthcare_system.git
cd healthcare_system
2. Set up a virtual environment
It’s recommended to use a virtual environment to manage your project dependencies.

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure the database
Update your settings.py with the appropriate PostgreSQL database settings:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5. Apply migrations
bash
Copy code
python manage.py migrate
6. Create a superuser
Create an admin account to access the Django admin interface:

bash
Copy code
python manage.py createsuperuser
7. Run the development server
Start the Django development server:

bash
Copy code
python manage.py runserver
8. Setting up Celery and Redis
Install Redis
If Redis is not installed, install it using Homebrew (for macOS):

bash
Copy code
brew install redis
brew services start redis
Or on Linux:

bash
Copy code
sudo apt-get install redis-server
sudo service redis start
Run Celery worker
Start the Celery worker to handle background tasks:

bash
Copy code
celery -A healthcare_system worker --loglevel=info
9. Run the Celery Beat scheduler (optional)
If you’re using periodic tasks (e.g., sending birthday greetings), you can run the Celery Beat scheduler:

bash
Copy code
celery -A healthcare_system beat --loglevel=info
10. Access the application
Open your browser and navigate to http://127.0.0.1:8000/ to access the application.

To access the Django admin panel, go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials you created earlier.

Usage
Client Management: Add and manage client details through the Django admin interface.
Appointment Scheduling: Schedule and view appointments from the admin panel.
Automated Messaging: The system automatically sends messages based on predefined triggers (birthdays, holidays, appointment reminders) via email.
Contributing
