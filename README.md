# HireHub 🚀

A modern Job Board & Recruitment Platform Backend built with Django REST Framework.

HireHub is a backend-focused recruitment system where employers can publish job opportunities and applicants can create resumes, apply for jobs, bookmark jobs, receive notifications, and manage their recruitment process through dashboards.

The project is built with real-world backend development practices including JWT authentication, role-based permissions, PostgreSQL database, API documentation, and production deployment.

---

# 🌐 Live Demo

API Base URL:

```
https://hirehub-api-3xms.onrender.com
```

Swagger Documentation:

```
https://hirehub-api-3xms.onrender.com/api/docs/
```

ReDoc:

```
https://hirehub-api-3xms.onrender.com/api/redoc/
```

OpenAPI Schema:

```
https://hirehub-api-3xms.onrender.com/api/schema/
```

---

# ✨ Features

## Authentication

- JWT Authentication
- Register / Login
- Refresh Token
- Custom User Model
- Role-based permissions

Supported roles:

- Applicant
- Employer


---

# Resume Management

Applicants can manage their professional profile:

- Create and update resume
- Manage skills
- Manage experiences
- Manage education
- Set employment status
- Set years of experience
- Set expected salary

Resume ownership validation is implemented to protect user data.

---

# Job Management

Employers can:

- Create jobs
- Update jobs
- Delete jobs
- Activate / deactivate jobs
- Manage their own job listings


Features:

- Employer ownership validation
- Job filtering
- Searching
- Ordering


Supported filters:

- Job Type
- Experience Level
- Salary Range


Ordering:

- Created date
- Salary
- Title


---

# Applications

Applicants can:

- Apply for jobs
- Track application status


Employers can:

- View received applications
- Review applicants
- Change application status


Application workflow:

```
Applied
    |
Under Review
    |
Interview
    |
Accepted / Rejected
```


Validation features:

- Prevent duplicate applications
- Prevent applying for own job
- Validate resume ownership


---

# Notifications

Automatic notifications are created for:

- New job applications
- Application status changes


Features:

- List notifications
- Read notifications
- Manage notification status


---

# Bookmarks

Applicants can:

- Save favorite jobs
- View saved jobs
- Remove bookmarks


Features:

- Prevent duplicate bookmarks
- User-specific bookmarks


---

# Dashboard

## Applicant Dashboard

Includes:

- Total applications
- Application status statistics
- Recent applications


## Employer Dashboard

Includes:

- Total jobs
- Active jobs
- Closed jobs
- Total applications
- Recent jobs
- Recent applicants


---

# 🛠 Tech Stack

## Backend

- Python 3.12
- Django 5.2
- Django REST Framework


## Database

- PostgreSQL


## Authentication

- Simple JWT


## API Documentation

- drf-spectacular
- Swagger UI


## Deployment

- Render
- Gunicorn
- WhiteNoise


## Development Tools

- Docker
- Docker Compose
- Git
- Linux


---

# 📂 Project Structure

```
HireHub/

├── apps/
│
├── accounts/
├── jobs/
├── resumes/
├── applications/
├── bookmarks/
├── notifications/
├── dashboard/
│
├── config/
│
├── docker/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/amirgoli1383saransari/hirehub.git
```

Go to project:

```bash
cd hirehub
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Linux:

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create `.env` file:

```env
DEBUG=True

SECRET_KEY=your-secret-key

POSTGRES_DB=database_name
POSTGRES_USER=database_user
POSTGRES_PASSWORD=password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

---

## Run Database Migrations

```bash
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run Development Server

```bash
python manage.py runserver
```

---

# 🐳 Docker Development

Docker is used for development environment setup.

Run:

```bash
cd docker
```

```bash
docker compose up --build
```

Run migrations:

```bash
docker compose exec web python manage.py migrate
```

Create superuser:

```bash
docker compose exec web python manage.py createsuperuser
```

---

# 🔐 Authentication

After login, add JWT token to requests:

```
Authorization: Bearer <access_token>
```

---

# 📌 Main API Endpoints


## Authentication

```
POST /api/accounts/register/

POST /api/token/

POST /api/token/refresh/
```


---

## Jobs

```
GET    /api/jobs/

POST   /api/jobs/

GET    /api/jobs/{id}/

PATCH  /api/jobs/{id}/

DELETE /api/jobs/{id}/
```


---

## Resume

```
GET    /api/resume/me/

PATCH  /api/resume/me/

GET    /api/resume/skills/

POST   /api/resume/skills/
```


---

## Applications

```
GET   /api/applications/

POST  /api/applications/

GET   /api/applications/jobs/{job_id}/applications/

PATCH /api/applications/{id}/status/
```


---

## Bookmarks

```
GET    /api/bookmarks/

POST   /api/bookmarks/

DELETE /api/bookmarks/{id}/
```


---

## Notifications

```
GET    /api/notifications/

PATCH  /api/notifications/{id}/read/

POST   /api/notifications/read-all/
```


---

## Dashboard

```
GET /api/dashboard/applicant/

GET /api/dashboard/employer/
```

---

# 🚀 Deployment

The project is deployed on Render.

Deployment stack:

- Render Web Service
- Render PostgreSQL
- Gunicorn WSGI Server
- WhiteNoise Static Files


Deployment workflow:

```
GitHub Push
      |
      |
Render Build
      |
      |
Install Dependencies
      |
      |
Collect Static Files
      |
      |
Run Migrations
      |
      |
Gunicorn Server
```

---

# 🔮 Future Improvements

- Email Notifications
- Celery + Redis Background Tasks
- Real-time Notifications with WebSocket
- Company Profile Pages
- Advanced Resume Builder
- Job Recommendation System
- Automated Testing
- CI/CD Pipeline


---

# 👨‍💻 Author

**Amir Mahdi Gol Mohammadi**

Backend Developer


Skills:

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Redis
- Clean Architecture


---

# 📦 Version

```
v1.0.0
```

---

# 📄 License

MIT License