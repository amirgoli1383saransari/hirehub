# HireHub

A modern Job Board & Recruitment Platform built with Django REST Framework.

HireHub is a backend-focused recruitment system where employers can publish jobs and applicants can build resumes, apply for positions, bookmark jobs, receive notifications, and manage their recruitment process through dashboards.

---

# Features

### Authentication

- JWT Authentication
- Login / Register
- Refresh Token
- Role-based permissions
- Applicant & Employer accounts

---

### Resume Management

- Create Resume
- Update Resume
- Delete Resume
- Resume ownership validation

---

### Job Management

- Create Job
- Edit Job
- Delete Job
- Activate / Deactivate Job
- Employer ownership validation

---

### Job Search

- Full-text Search
- Filter by:

  - Job Type
  - Experience Level
  - Salary Range

- Ordering by:

  - Date
  - Salary
  - Title

---

### Applications

Applicants can

- Apply for Jobs
- Track Application Status

Employers can

- View Applicants
- Review Applications
- Accept Applicants
- Reject Applicants
- Schedule Interviews

---

### Notifications

Automatic notifications when

- Someone applies for your job
- Application status changes

Features

- List Notifications
- Mark One as Read
- Mark All as Read

---

### Bookmarks

Applicants can

- Save Jobs
- View Saved Jobs
- Remove Saved Jobs

---

### Dashboard

Applicant Dashboard

- Total Applications
- Under Review
- Accepted
- Rejected
- Recent Applications

Employer Dashboard

- Total Jobs
- Active Jobs
- Closed Jobs
- Total Applications
- Recent Jobs
- Recent Applicants

---

# Tech Stack

- Python 3.12
- Django 5
- Django REST Framework
- PostgreSQL
- Docker
- Docker Compose
- JWT Authentication
- drf-spectacular (Swagger)
- django-filter

---

# Project Structure

```
HireHub/

apps/
    accounts/
    jobs/
    resumes/
    applications/
    bookmarks/
    notifications/
    dashboard/

config/

docker/

requirements.txt
```

---

# API Documentation

Swagger

```
http://localhost:8000/api/docs/
```

ReDoc

```
http://localhost:8000/api/redoc/
```

OpenAPI Schema

```
http://localhost:8000/api/schema/
```

---

# Running with Docker

Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/HireHub.git
```

Go inside project

```bash
cd HireHub/docker
```

Build

```bash
docker compose up --build
```

Run migrations

```bash
docker compose exec web python manage.py migrate
```

Create Superuser

```bash
docker compose exec web python manage.py createsuperuser
```

---

# Running Locally

Create virtual environment

```bash
python -m venv .venv
```

Activate

Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python manage.py migrate
python manage.py runserver
```

---

# Main Endpoints

Authentication

```
POST /api/accounts/register/
POST /api/accounts/login/
POST /api/token/refresh/
```

Jobs

```
GET /api/jobs/
POST /api/jobs/
GET /api/jobs/{id}/
PATCH /api/jobs/{id}/
DELETE /api/jobs/{id}/
```

Applications

```
GET /api/applications/
POST /api/applications/
PATCH /api/applications/{id}/status/
```

Bookmarks

```
GET /api/bookmarks/
POST /api/bookmarks/
DELETE /api/bookmarks/{id}/
```

Notifications

```
GET /api/notifications/
PATCH /api/notifications/{id}/read/
POST /api/notifications/read-all/
```

Dashboard

```
GET /api/dashboard/applicant/
GET /api/dashboard/employer/
```

---

# Future Improvements

- Email Notifications
- Celery + Redis
- Real-time Notifications (WebSocket)
- Company Profiles
- Advanced Resume Builder
- Job Recommendation Engine
- Unit Tests
- CI/CD Pipeline
- Deployment

---

# Version

Current Release

```
v1.0.0
```

---

# License

MIT License