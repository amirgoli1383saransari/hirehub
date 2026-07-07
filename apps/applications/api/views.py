from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.notifications.models import Notification
from apps.notifications.services import create_notification
from apps.accounts.permissions import (
    IsApplicant,
    IsEmployer,
)

from apps.applications.models import Application
from apps.jobs.models import Job

from apps.notifications.services import create_notification

from .serializers import (
    ApplicationSerializer,
    EmployerApplicationSerializer,
    ApplicationStatusSerializer,
)


# =========================
# Applicant: Apply for Job
# =========================
class ApplicationListCreateView(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [
        IsAuthenticated,
        IsApplicant,
    ]

    def get_queryset(self):
        return (
            Application.objects
            .filter(applicant=self.request.user)
            .select_related(
                "job",
                "resume",
                "applicant",
            )
        )

    def perform_create(self, serializer):
        application = serializer.save(
            applicant=self.request.user
        )

        # 🔔 Notify Employer
        create_notification(
            user=application.job.owner,
            title="New Application",
            message=(
                f"{application.applicant.email} applied "
                f"for {application.job.title}"
            ),
            notification_type="application",
        )


# =========================
# Employer: View Applications of a Job
# =========================
class JobApplicationsView(generics.ListAPIView):
    serializer_class = EmployerApplicationSerializer

    permission_classes = [
        IsAuthenticated,
        IsEmployer,
    ]

    def get_queryset(self):
        job = get_object_or_404(
            Job,
            id=self.kwargs["job_id"],
            owner=self.request.user,
        )

        return (
            Application.objects
            .filter(job=job)
            .select_related(
                "applicant",
                "resume",
            )
        )


# =========================
# Employer: Update Application Status
# =========================
class ApplicationStatusUpdateView(generics.UpdateAPIView):
    serializer_class = ApplicationStatusSerializer

    permission_classes = [
        IsAuthenticated,
        IsEmployer,
    ]

    def get_queryset(self):
        return (
            Application.objects
            .filter(job__owner=self.request.user)
            .select_related(
                "job",
                "applicant",
            )
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        old_status = instance.status

        response = super().update(request, *args, **kwargs)

        # مقدار جدید بعد از ذخیره
        instance.refresh_from_db()

        if old_status != instance.status:
            create_notification(
                user=instance.applicant,
                title="Application Status Updated",
                message=(
                    f"Your application for "
                    f"{instance.job.title} is now "
                    f"{instance.get_status_display()}."
                ),
                notification_type="status_update",
            )

        return response