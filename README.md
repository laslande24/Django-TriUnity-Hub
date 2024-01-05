# Django Multi-App Project

Welcome to the Django Multi-App Project! This project includes three apps: a blog app, a weather app, and a chat room app.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/laslande24/Django-TriUnity-Hub.git

2. Navigate to the project directory:
     ```bash
     cd django-multi-app-project
     
4. Create a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     
6. Activate the virtual environment:
    On Windows (Command Prompt):
     ```bash
     .\venv\Scripts\activate
     
   On macOS/Linux:
     ```bash
     source venv/bin/activate
     
7. Install dependencies:
     ```bash
     pip install -r requirements.txt
   
### Database Setup

1. Apply database migrations:
     ```bash
     python manage.py migrate
   
2. Create a superuser (admin) account:
    ```bash
    python manage.py createsuperuser

3. Running the Development Server
    ```bash
    python manage.py runserver
