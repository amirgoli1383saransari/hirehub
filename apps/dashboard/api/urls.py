from django.urls import path

from .views import (
    ApplicantDashboardView,
    EmployerDashboardView,
)

urlpatterns = [
    # Applicant Dashboard
    path(
        "applicant/",
        ApplicantDashboardView.as_view(),
        name="applicant-dashboard",
    ),

    # Employer Dashboard
    path(
        "employer/",
        EmployerDashboardView.as_view(),
        name="employer-dashboard",
    ),
]