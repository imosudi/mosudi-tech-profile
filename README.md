# Mosudi Tech Profile
**Personal tech profile built with Flask, Bootstrap 5.3.8 and SQLite**  
Personal tech profile built with Flask, Bootstrap 5, and SQLite — showcasing software development, infrastructure engineering, and IoT expertise by **Isiaka Olukayode Mosudi**.


- Repository: `https://github.com/imosudi/mosudi-tech-profile`  
- Website / domain (planned): `https://mioemi.com`  
- Contact: `imosudi@outlook.com`

---

## Overview

**Mosudi Tech Profile** is a compact, secure and responsive personal portfolio web application built with Flask. It provides:

- A responsive front-end (Bootstrap 5.3.8)
- A lightweight SQLite data store for projects and basic content
- Secure authentication using `flask-security-too`
- A contact form protected by Flask-WTF CSRF
- Extensible structure for projects, blog posts and admin content

This repository is intended as a minimal, deployable portfolio you can adapt and extend.

---

## Tech stack

- **Backend:** Flask (Python)  
- **Frontend:** HTML5, Bootstrap 5.3.8, JavaScript  
- **Database:** SQLite (development)  
- **Auth:** `flask-security-too`  
- **Forms:** Flask-WTF  
- **Environment:** Python 3.10+ (3.11/3.12 supported)  
- **Licence:** BSD 2-Clause

---

## Features

- Landing page (hero, skills, featured projects)
- Projects listing and placeholder detail actions
- About and Contact pages with secured form
- User authentication and role support (admin/editor)
- Clear, modular codebase for easy extension

---

## Quick start (development)

> Tested with Python 3.10 — 3.12. Use a virtual environment.

1. **Clone the repo**
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

4. **Create `.env` file**
```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=replace_with_a_secure_secret
DATABASE_URL=sqlite:///mosudi_tech_profile.db
SECURITY_PASSWORD_SALT=replace_with_a_password_salt
MAIL_SERVER=localhost
MAIL_PORT=25
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_USE_TLS=False
```

5. **Initialise the database and run**
```bash
python app.py
```

Access on `http://127.0.0.1:5000/`

---

## Licence

BSD 2-Clause License

Copyright (c) 2025, Isiaka Olukayode Mosudi
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

---

## Author

**Isiaka Olukayode Mosudi**  
Vienna, Austria  
Email: `imosudi@outlook.com`  
GitHub: [https://github.com/imosudi](https://github.com/imosudi)  
Website: `https://mioemi.com`