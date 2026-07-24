# 🌐 Portfolio | Personal Digital Portfolio Web App

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![React Native Goal](https://img.shields.io/badge/React_Native-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-3.4-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

Welcome to **Portfolio** — a clean, modern, and beginner-friendly personal portfolio web application built with **Python & Django**. Designed to showcase coding projects, learning milestones, study notes, and personal skills in a sleek dark-mode web application.

---

## ✨ Features

- 👤 **Student & Developer Hero**: Personalized profile with student badges (`💻 Web Development`, `📚 Coding Enthusiast`) and clean silhouette avatar placeholder.
- 🗺️ **The Build Chronicles**: Interactive timeline tracking learning milestones (`intro.md` ➔ `Portfolio` ➔ `Anulekh Project`).
- ✍️ **Active Working Project**: Highlights **Anulekh Project** — an intelligent note-taking application built with **React Native & Django**, with a future goal to learn **Rust**.
- 🔨 **Project Showcase**: Clean grid exhibiting beginner projects (Task Manager, Portfolio, Anulekh).
- 📝 **The Codex Blog**: Tech articles & study notes on Python fundamentals, web development, and coding logic.
- ⚙️ **Admin Dashboard**: Built-in admin templates to manage profile details and project showcases.
- 🎨 **Modern Aesthetics**: Built with Tailwind CSS, Alpine.js, Lucide Icons, and dark-mode glassmorphism.

---

## 📁 Repository Structure

```text
Portfolio/
├── config/                 # Django settings, URLs, and WSGI entry point
├── core/                   # Main application logic & home views
│   ├── templates/          # Homepage & partials (navbar, footer, hero)
│   └── views.py            # Core view controllers
├── templates/              # Site templates (about, projects, portfolio, blogs, contact, admin)
├── static/                 # Static assets (icons, CSS, JavaScript)
├── db.sqlite3              # SQLite local database
├── manage.py               # Django execution script
└── requirements.txt        # Python dependencies list
```

---

## 🛠️ Local Development Setup

Follow these simple steps to run the project locally on your machine:

### 1. Clone the repository
```bash
git clone https://github.com/mrveer-101/Portfolio.git
cd Portfolio
```

### 2. Create and activate virtual environment
- **Windows (PowerShell)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
- **Mac / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run development server
```bash
python manage.py runserver
```

Open your browser and visit: **`http://127.0.0.1:8000/`**

---

## 🌐 Hosting Guide: Deploy to PythonAnywhere (Free)

This project is pre-configured for simple, zero-config deployment on **PythonAnywhere**:

1. **Sign Up**: Create a free account at [PythonAnywhere](https://www.pythonanywhere.com/).
2. **Open Bash Console**: Clone the repository:
   ```bash
   git clone https://github.com/mrveer-101/Portfolio.git
   ```
3. **Set up Virtualenv**:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   ```
4. **Configure Web App**:
   - Set **Source Code Path**: `/home/yourusername/Portfolio`
   - Set **Virtual environment**: `/home/yourusername/.virtualenvs/myenv`
   - Set **WSGI Configuration file**: point `application` to `config.wsgi.application`.
5. **Collect Static Files**:
   ```bash
   python manage.py collectstatic --noinput
   ```
6. Click **Reload** on PythonAnywhere to go live!

---

## 👤 Author

**Veer Patel**
- 🎓 11th Grade Commerce Student | Learning Python & Web Development
- 🐙 GitHub: [@mrveer-101](https://github.com/mrveer-101)
- 📧 Email: [mrveerp16@gmail.com](mailto:mrveerp16@gmail.com)

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
