# NIRVAN | Digital Portfolio Engine

![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-3.4-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![HTMX](https://img.shields.io/badge/HTMX-1.9-336699?style=for-the-badge&logo=htmx&logoColor=white)
![AlpineJS](https://img.shields.io/badge/Alpine.js-3.x-8BC0D0?style=for-the-badge&logo=alpine.js&logoColor=white)

**NIRVAN** is a high-performance, premium personal portfolio engine built using the modern Python stack. It leverages Server-Side Rendering (SSR) for superior SEO and performance, while using HTMX and Alpine.js to provide a fluid, single-page application experience.

## 🚀 Key Features
- **Modern Tech Stack**: Django 6.0+, HTMX, Alpine.js, and Tailwind CSS (D-A-H-T stack).
- **Premium Aesthetic**: Sleek dark mode with glassmorphic UI elements and smooth micro-animations.
- **Optimized for SEO**: Full server-side rendering for lightning-fast indexing and performance.
- **Component-Based**: Modular template architecture using `django-cotton`.
- **Developer Friendly**: Pre-configured with VS Code auto-activation and browser-reload.

## 🏗️ Project Architecture
```text
NIRVAN/
├── core/               # Main application logic
├── nirvan/             # Project configuration & settings
├── static/             # Global static assets (CSS, JS, Images)
├── templates/          # Global base templates
├── venv/               # Virtual environment
└── manage.py           # Django entry point
```

## 🛠️ Getting Started

### Prerequisites
- Python 3.10+
- Git

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/ArionGD/NIRVAN.git
   cd NIRVAN
   ```

2. **Setup Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

## 🎨 Design Philosophy
NIRVAN follows a "Obsidian Glass" design philosophy—prioritizing deep contrast, subtle gradients, and high-quality typography to ensure your work stands out with a professional and modern look.

## 📄 License
This project is licensed under the MIT License.
