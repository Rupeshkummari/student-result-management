# Student Result Management System

A full-stack web application to manage student records, academic results, and subject details — built with Django and Python.

## Screenshots

> Dashboard, student list, result entry, and public result lookup views.

## Tech Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Frontend  | HTML5, CSS3, Bootstrap, JavaScript |
| Backend   | Python 3.12, Django 5.1           |
| Database  | SQLite3 (easily switchable to MySQL) |
| Auth      | Django built-in authentication    |
| Tools     | Postman, Git, VS Code             |

## Features

- Role-based access control — Admin login with protected dashboard
- Student CRUD — Add, view, edit, delete student records
- Student photo upload and profile display
- Subject management
- Result entry with grade and marks per subject per semester
- Public result lookup — Students can check results by roll number
- Search and filter students by name or department
- Django Admin panel for backend management

## Project Structure

```
student-result-management/
├── core/
│   ├── manage.py
│   └── core/
│       ├── settings.py
│       ├── urls.py
│       ├── wsgi.py
│       └── asgi.py
├── results/
│   ├── models.py       # Student, Subject, Result models
│   ├── views.py        # All CRUD and auth views
│   ├── urls.py         # URL routing
│   ├── admin.py        # Admin panel config
│   └── templates/
│       └── results/    # HTML templates
├── templates/
│   └── static/
│       ├── css/
│       └── js/
├── requirements.txt
└── .gitignore
```

## Setup and Run Locally (Windows CMD)

**1. Clone the repository (or navigate to your project folder)**
```cmd
cd path\to\your\student-result-management
cd core
```

**2. Create and activate the virtual environment**
```cmd
python -m venv env
env\Scripts\activate
```
*(You will know it is activated when you see `(env)` at the beginning of your CMD prompt).*

**3. Install dependencies**
```cmd
pip install -r ..\requirements.txt
pip install Pillow
```

**4. Run migrations & Create Admin**
```cmd
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
*(Follow the prompt to set your admin username and password).*

**5. Start the server**
```cmd
python manage.py runserver
```
Visit: `http://127.0.0.1:8000`

---

## How to Push to GitHub

Once you are completely done with all local changes, run these exact commands in CMD from the absolute root of your project:

```cmd
git add .
git commit -m "Complete professional frontend UI redesign with Bootstrap"
git branch -M main
git push -u origin main
```

## Developer

**Rupesh K**
- GitHub: [github.com/Rupeshkummari](https://github.com/Rupeshkummari)
- LinkedIn: [linkedin.com/in/kummari-rupesh-76325a251](https://linkedin.com/in/kummari-rupesh-76325a251)
- Email: rupeshkummari223@gmail.com
