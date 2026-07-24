# Portfolio | Personal Web Portfolio

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-3.4-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

**Portfolio** is a clean, simple, and beginner-friendly personal web portfolio built with Python and Django. Designed to showcase projects, coding notes, and skills in a modern dark-themed web application.

---

## 🚀 Features

- **Simple Tech Stack**: Built with Python, Django, HTML, Tailwind CSS, and Alpine.js.
- **Beginner Friendly**: Clean project layout and easy setup for learning Python web development.
- **Responsive Design**: Looks great on both desktop and mobile screens.
- **Easy Hosting**: Pre-configured for free hosting on platforms like **PythonAnywhere**.

---

## 📁 Project Structure

```text
Portfolio/
├── config/             # Django settings & routing
├── core/               # Main app views & templates
├── static/             # CSS & image assets
├── templates/          # Web page templates
└── manage.py           # Django execution script
```

---

## 🛠️ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/mrveer-101/Portfolio.git
cd Portfolio
```

### 2. Set up virtual environment
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run local server
```bash
python manage.py runserver
```

Open your browser at `http://127.0.0.1:8000/`.

---

## 🌐 Hosting on PythonAnywhere

1. Upload or clone repository to PythonAnywhere.
2. Create a virtual environment and install `requirements.txt`.
3. Set the WSGI configuration to `config.wsgi`.
4. Run `python manage.py collectstatic`.

---

## 📄 License
MIT License
