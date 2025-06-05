# 📰 Django Blog – Post View + Pytest Architecture

This project was developed during the Full Stack Python program at [EBAC](https://ebaconline.com.br/), with a focus on Django fundamentals, modular project structure, and test-driven development using Pytest.

It simulates a minimal blog system with a functional Post view, structured templates, Django admin configuration, and automated tests for quality assurance.

---

## 🧱 Project Structure

mysite/
├── blog/
│ ├── models/
│ ├── templates/blog/
│ ├── views.py
│ ├── urls.py
│ ├── admin.py
│ └── factories.py
├── tests/
│ └── pytest-based unit tests
└── manage.py


---

## 🚀 Key Features

- Modular Django app architecture
- `PostView` with connected templates
- Django Admin integration
- Pytest test suite with Factory Boy
- Custom URL routing
- Project bootstrapped with clean settings and environment control

---

## 🛠️ Tech Stack

- **Python 3.12**
- **Django 4.x**
- **Pytest**
- **Factory Boy**
- **HTML / Django Templating**

---

## 🧪 Running Tests

Create your virtual environment and install dependencies:

```bash
pip install -r requirements.txt

Then, run the test suite using:

pytest

Tests are located in the /tests folder and are based on Factory Boy and PostView coverage.
📚 Learning Highlights

- Modular separation of Django apps (blog, mysite)

- Views and templates following Django conventions

- Reusable factory classes for test data

- Pytest configuration for scalable testing

- Version control discipline (semantic commits and project structure)

✅ Status

✔️ In Progress – Foundation complete, open for future improvements like models, authentication, and REST API integration.

    📌 Educational project developed to solidify Django core concepts and testing discipline using Pytest.
