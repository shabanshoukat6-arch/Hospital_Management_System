 
# 🏥 MedFlow — Hospital Management System

A modern and responsive **Hospital Management System (HMS)** built with Python and Django. MedFlow provides a centralized dashboard for managing patient records, doctor information, and hospital appointments through a clean, professional interface.

## ✨ Features

- **Authentication:** Secure login and logout using Django's authentication system.
- **Interactive Dashboard:** Modern hospital-themed interface with smooth animations and responsive layouts.
- **Patient Management:** Add, view, update, and delete patient records.
- **Doctor Management:** Store doctor information, specializations, and availability.
- **Appointment Management:** Maintain appointment records, including patients, doctors, dates, and status.
- **Dashboard Statistics:** Display patient counts, doctor counts, total appointments, and scheduled appointments.
- **Recent Appointments:** View recent appointment records with patient and doctor details.
- **Django ORM:** Manage database operations using Django models.
- **Admin Panel:** Manage registered models through Django's built-in administration interface.
- **Responsive Design:** Dashboard layout adapts to desktop, tablet, and mobile screens.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| SQLite | Development database |
| HTML5 | Page structure |
| CSS3 | Styling, animations, and responsive design |
| Django ORM | Database operations |
| Django Authentication | User login and logout |
| Git & GitHub | Version control and project hosting |

## 📁 Project Structure

```text
hospital_management/
│
├── hospital_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── core/
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       ├── login.html
│   │       ├── dashboard.html
│   │       ├── patient_list.html
│   │       ├── patient_form.html
│   │       └── patient_confirm_delete.html
│   │
│   ├── static/
│   │   └── core/
│   │       └── css/
│   │           └── style.css
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── db.sqlite3
└── README.md
```

*Note: The structure above represents the intended project organization. Your actual files may differ as development continues.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd hospital_management
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
venv\Scripts\activate
```

### 4. Install Django

```bash
python -m pip install django
```

### 5. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

If migrations are already included in the repository, running `python manage.py migrate` is generally sufficient.

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin credentials.

### 7. Start the development server

```bash
python manage.py runserver
```

Open the following URLs in your browser:

- **Login:** http://127.0.0.1:8000/login/
- **Dashboard:** http://127.0.0.1:8000/dashboard/
- **Admin Panel:** http://127.0.0.1:8000/admin/

The dashboard requires authentication. Create a superuser and ensure the login page is configured to authenticate that account.

## 🗄️ Database Models

The application includes the following core models:

### Patient
Stores patient details, including name, age, gender, contact information, address, and registration date.

### Doctor
Stores doctor details, including name, medical specialization, contact information, and availability.

### Appointment
Connects patients with doctors and records appointment dates, reasons, and statuses.

**Appointment statuses:**
- Scheduled
- Completed
- Cancelled

## 🔐 Authentication and Security

The project uses Django's built-in authentication features for login and logout, along with protected dashboard and patient-management views.

Additional production security measures, such as HTTPS, secure cookie settings, environment-based secrets, and appropriate staff permissions, should be configured before deployment.

## 🎨 User Interface

The dashboard includes:

- A professional navigation sidebar
- Hospital overview banner
- Statistics cards connected to database counts
- Recent appointment table
- Patient management shortcuts
- Responsive layout and CSS animations
- Appointment status indicators

## 🚀 Future Improvements

- Doctor management pages with full CRUD operations
- Appointment booking and management interface
- Search, filtering, and pagination
- Patient medical history
- Billing and payment management
- Role-based permissions for administrators, doctors, and receptionists
- Interactive analytics charts
- PostgreSQL integration
- Deployment to a production server

## 👨‍💻 Developer

**Muhammad Shaban Shoukat**

Python | Django | Web Development

## 📄 License

This project is intended for learning and development. Add a suitable open-source license if you plan to distribute or reuse it publicly.
