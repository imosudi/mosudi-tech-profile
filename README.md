# Mosudi Tech Profile

![Flask](https://img.shields.io/badge/Flask-3.0-blue?logo=flask)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.8-purple?logo=bootstrap)
![License](https://img.shields.io/badge/License-BSD_2--Clause-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🖼️ Preview

| Desktop View | Mobile View |
|---------------|--------------|
|![alt Desktop Preview](images/preview-desktop.png) |![alt  Mobile Preview](images/preview-mobile.png)|

---

## 📁 Repository & Contact

- **Repository:** [https://github.com/imosudi/mosudi-tech-profile](https://github.com/imosudi/mosudi-tech-profile)  
- **Planned Domain:** [https://mioemi.com](https://mioemi.com)  
- **Contact:** `imosudi@outlook.com`

---

## 🧭 Overview

**Mosudi Tech Profile** is a compact, secure, and modular Flask web application designed to serve as a digital technical résumé and project portfolio.  
It provides a simple yet scalable structure for personal branding, research dissemination, and portfolio demonstration.

The project includes:

- Responsive Bootstrap 5.3.8 front-end
- SQLite database (via Flask-SQLAlchemy)
- Secure authentication with `flask-security-too`
- Contact form with CSRF protection (Flask-WTF)
- Modular structure for projects, blogs, and future admin extensions
- WSGI-ready deployment (`main.wsgi`)

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend** | Flask 3.x (Python 3.10+) |
| **Frontend** | HTML5, Jinja2, Bootstrap 5.3.8, JavaScript |
| **Database** | SQLite (development) |
| **Authentication** | Flask-Security-Too |
| **Forms & Validation** | Flask-WTF |
| **Email Support** | Flask-Mail |
| **Environment** | Python 3.10 – 3.12 |
| **Licence** | BSD 2-Clause |

---

## ✨ Features

- 🏠 Landing page highlighting skills, research areas, and featured projects  
- 🧠 Projects listing (adaptive IoT systems, analytics tools, research frameworks, etc.)  
- 📄 Modular templates for About, Contact, and future Blog sections  
- 🔒 Secure user authentication with role-based access (admin/editor)  
- ⚙️ Lightweight SQLite data persistence  
- 📦 Structured, extensible Flask blueprint architecture  
- ☁️ WSGI-ready for deployment on Apache, Nginx + Gunicorn, or PythonAnywhere  

---

## 🏗️ Project Structure

```
mosudi-tech-profile/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   └── templates/
├── images/
│   ├── preview-desktop.png
│   └── preview-mobile.png
├── instance/
│   └── mosudi_tech_profile.db
├── main.py
├── main.wsgi
├── requirements.txt
├── README.md
└── venv/
```

> The `app/` directory contains all core Flask logic, static assets, and templates.  
> The `instance/` folder holds the SQLite database and can store environment-specific configuration.

---

## 🚀 Quick Start (Development)

> Verified on Python 3.10 – 3.12

1. **Clone the repository**
```bash
git clone https://github.com/imosudi/mosudi-tech-profile.git
cd mosudi-tech-profile
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create an `.env` file**
```env
FLASK_APP=main.py
FLASK_ENV=development
SECRET_KEY=replace_with_a_secure_secret
DATABASE_URL=sqlite:///instance/mosudi_tech_profile.db
SECURITY_PASSWORD_SALT=replace_with_a_password_salt
MAIL_SERVER=localhost
MAIL_PORT=25
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_USE_TLS=False
```

5. **Initialise and run**
```bash
python main.py
```

Access locally at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🌐 Deployment

This application is production-ready using **WSGI**.

- **Apache / mod_wsgi:** Use `main.wsgi`  
- **Gunicorn / Nginx:**
  ```bash
  gunicorn -w 4 -b 0.0.0.0:5000 main:app
  ```

Ensure environment variables and database paths are correctly set before deployment.

---

## 🧩 Future Extensions

- Admin dashboard for project and post management  
- Integration of IoT visual dashboards (Grafana / Flask Charts)  
- REST API endpoints for project and research data  
- Blog system with Markdown support  
- Internationalisation (English, French planned)

---

## 🪪 Licence

**BSD 2-Clause License**

Copyright © 2025  
**Isiaka Olukayode Mosudi**

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.  
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

> THIS SOFTWARE IS PROVIDED “AS IS” WITHOUT WARRANTY OF ANY KIND.

---

## 👤 Author

**Isiaka Olukayode Mosudi**  
M.Eng (Communications Engineering) | MSc (IoT & Smart Systems)  
Vienna, Austria  

📧 `imosudi@outlook.com`  
🌐 [https://mioemi.com](https://mioemi.com)  
💻 [https://github.com/imosudi](https://github.com/imosudi)
