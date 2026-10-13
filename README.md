
# 📚 School Attendance & Grades Platform
**منصة متابعة الحضور والدرجات للمدارس والسناتر**

A web platform that lets teachers record attendance and grades in under a minute, parents follow their child from their phone, and managers see the whole school at a glance. Fully Arabic (RTL), mobile-first, and installable as an app on Android and iPhone.

منصة تسهّل على المدرس تسجيل الحضور والدرجات، وعلى ولي الأمر متابعة ابنه من الموبايل، وعلى المدير متابعة المدرسة كلها.

## ✨ Features

**👩‍🏫 Teachers**
- Take attendance per class and date (present / absent / late), with a "mark all present" shortcut
- Enter grades for a whole class at once
- Each teacher sees only their own classes

**👨‍👩‍👧 Parents**
- Private dashboard: only their own children
- Attendance rate, absences, average grade, and performance level
- Charts for grades and attendance

**🧑‍💼 Managers**
- Daily summary: today's attendance rate and who is absent
- Most absent students and attendance rate per class
- Monthly attendance report exported to Excel
- Bulk-import students from Excel (parent accounts are created automatically)
- Manage teachers and assign classes

**📱 Installable app (PWA)** — opens full-screen from the phone's home screen, no link needed.

## 🛠 Tech stack
Python · Django 5.2 · SQLite · Chart.js · openpyxl (Excel) · PWA (manifest + service worker) · HTML/CSS (responsive, RTL)

## 🚀 Run locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Optional demo data (2 classes, 16 students, a month of attendance and grades):

```bash
python manage.py seed_demo
```

### Environment variables (production)

| Variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | Secret key |
| `DJANGO_DEBUG` | `0` in production |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated hosts |
| `DJANGO_CSRF_ORIGINS` | Trusted HTTPS origins |

## 🔐 Security
Role-based access (manager / teacher / parent), parents can only read their own children's data, teachers can only edit their own classes, password change for all users, and secure cookies in production.

## 🗺 Roadmap
- WhatsApp / SMS absence alerts to parents
- PDF reports
- Per-school branding (name, colors, logo)
- Native mobile app

## 👩‍💻 Author
Built by **Rewan Ahmed**.