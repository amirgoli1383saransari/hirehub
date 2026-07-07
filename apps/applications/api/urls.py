from django.urls import path

from .views import (
    ApplicationListCreateView,
    JobApplicationsView,
    ApplicationStatusUpdateView,
)

urlpatterns = [
    path(
        "",
        ApplicationListCreateView.as_view(),
        name="application-list-create",
    ),

    path(
        "jobs/<int:job_id>/applications/",
        JobApplicationsView.as_view(),
        name="job-applications",
    ),

    path(
        "<int:pk>/status/",
        ApplicationStatusUpdateView.as_view(),
        name="application-status",
    ),
]