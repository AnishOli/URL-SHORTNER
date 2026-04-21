# URL Shortener (Django)

A simple URL Shortener web application built using Django.  
It converts long URLs into short, shareable links and tracks basic click analytics.

---

## Features

- Generate short URLs from long links
- Redirect short URLs to original URLs
- Track click counts for each link
- Simple and minimal UI
- Built using Django ORM and SQLite

---

## Tech Stack

- Python
- Django
- SQLite
- HTML / CSS

---

## How It Works

1. User submits a long URL
2. System generates a unique slug
3. URL is stored in the database
4. Short URL redirects to original URL
5. Click count increases on each visit

---

##Project Structure
```
urlShort/
│
├── url/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── urlapp/
│           └── index.html
│
├── urlShort/
│   ├── settings.py
│   ├── urls.py
│
└── db.sqlite3
│
└── db.sqlite3
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/AnishOli/URL-SHORTNER.git
cd URL-SHORTNER
```
### 2. Create virtual environment
#### Activate virtual environment:
```bash
python -m venv myenv
```
#### Windows
```bash
myenv\Scripts\activate
```
#### Mac/linux
```bash
source myenv/bin/activate
```
### 3. Install dependencies
```bash
pip install django
```
### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Run server
```bash
python manage.py runserver
```
#### Open in browser:
```bash
http://127.0.0.1:8000/
```
## Author
Anish Oli
Software Engineering Graduate | Django Developer
