# Implementation Plan: NIRVAN Portfolio Engine

Build a premium, high-performance personal portfolio using the **D-A-H-T** stack (Django, Alpine.js, HTMX, Tailwind CSS).

## 🚀 Tech Stack
- **Backend**: Django 6.x (SSR, robust ORM, Admin Panel)
- **Styling**: Tailwind CSS (Modern utility-first CSS)
- **Interactivity**: HTMX (AJAX without heavy JS)
- **Client Logic**: Alpine.js (Lightweight micro-animations and state)
- **Icons**: **Lucide Icons** (Professional/Minimalist SVG set)
- **Database**: SQLite (Dev) / **Neon.tech Postgres** (Prod - Always Free)
- **Hosting**: **Google Cloud Run** (Prod - Always Free / Scale to Zero)
- **Containerization**: **Docker** (For consistent deployment)

## 🎨 Design Vision (ORION Executive Aesthetic)
- **Branding**: ORION (Professional, High-Trust, Modern)
- **Theme**: Light-Mode Default (Glassmorphic) / Dark Mode Support.
- **Color Palette**: 
    - **Primary**: Professional Dark Blue (#1E40AF)
    - **Secondary**: Accent Orange (#FFA500)
- **Typography**: 
    - **Headings**: **Outfit** (Geometric, Bold)
    - **Body**: **Plus Jakarta Sans** (Premium, High-Legibility)
- **Style**: Dynamic background "shine spots", orbiting planetary icon systems.

## 🏗️ Core Modules
1. **Core**: General settings, Landing page, Navigation.
2. **Projects**: Portfolio gallery with categories, tech stacks, and links.
3. **Achievements**: Timeline-based achievements and certifications.
4. **Badges**: Interactive badge display (SVG-based).
5. **Experience**: Professional career timeline.

## 🛠️ Step-by-Step Roadmap

### Phase 1: Environment Setup & Dockerization ✅
- Initialize Django project and Core app.
- Configure VS Code auto-activation.
- **Set up Dockerfile and Docker Compose for local/prod parity.**
- **Configure environment variables (.env) for Neon DB.**

### Phase 2: Schema Development
- Create models for Project, Experience, Achievement, and Badge.
- Setup Django Admin for content management.

### Phase 3: UI Development (The "WOW" Factor)
- Implement OPPA-inspired Header, Hero, and Footer.
- Build the "Project Grid" with HTMX filtering.
- Implement glassmorphic components via Django-Cotton.

### Phase 4: Performance, SEO & Security
- Implement Meta tags and OpenGraph data.
- Setup WhiteNoise for static file serving in production.
- Optimize images and minify assets.

### Phase 5: Deployment (GCP Always Free)
- Configure `gcloud` CLI.
- Build and push Docker image to Artifact Registry.
- Deploy to Google Cloud Run with Neon Database connection.

## 📁 Directory Structure
```text
NIRVAN/
├── config/             # Project configuration (settings, urls, wsgi)
├── core/               # Main portfolio app (Logic & Templates)
├── static/             # Global assets (CSS, JS, Images)
├── .vscode/            # Editor settings
├── Dockerfile          # Container instructions
├── requirements.txt    # Python dependencies
└── manage.py           # Entry point
```
