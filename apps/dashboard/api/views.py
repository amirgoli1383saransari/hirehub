from django.db.models import Count, Q

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.permissions import (
    IsApplicant,
    IsEmployer,
)

from apps.jobs.models import Job
from apps.applications.models import Application


# =========================
# Applicant Dashboard
# =========================
class ApplicantDashboardView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsApplicant,
    ]

    def get(self, request):

        applications = (
            Application.objects
            .filter(applicant=request.user)
            .select_related("job")
        )

        stats = applications.aggregate(
            total_applications=Count("id"),

            # applied = waiting for review
            pending=Count(
                "id",
                filter=Q(status="applied"),
            ),

            under_review=Count(
                "id",
                filter=Q(status="under_review"),
            ),

            interview=Count(
                "id",
                filter=Q(status="interview"),
            ),

            accepted=Count(
                "id",
                filter=Q(status="accepted"),
            ),

            rejected=Count(
                "id",
                filter=Q(status="rejected"),
            ),
        )

        recent_applications = (
            applications
            .order_by("-created_at")[:5]
        )

        recent_data = [
            {
                "job_id": application.job.id,
                "title": application.job.title,
                "company": application.job.company,
                "status": application.status,
                "applied_at": application.created_at,
            }
            for application in recent_applications
        ]

        return Response(
            {
                **stats,
                "recent_applications": recent_data,
            }
        )


# =========================
# Employer Dashboard
# =========================
class EmployerDashboardView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsEmployer,
    ]

    def get(self, request):

        jobs = (
            Job.objects
            .filter(owner=request.user)
            .annotate(
                applications_count=Count(
                    "applications"
                )
            )
        )

        applications = (
            Application.objects
            .filter(job__owner=request.user)
            .select_related(
                "job",
                "applicant",
            )
        )

        job_stats = jobs.aggregate(
            total_jobs=Count("id"),

            active_jobs=Count(
                "id",
                filter=Q(is_active=True),
            ),

            closed_jobs=Count(
                "id",
                filter=Q(is_active=False),
            ),
        )

        app_stats = applications.aggregate(
            total_applications=Count("id"),

            pending=Count(
                "id",
                filter=Q(status="applied"),
            ),

            under_review=Count(
                "id",
                filter=Q(status="under_review"),
            ),

            interview=Count(
                "id",
                filter=Q(status="interview"),
            ),

            accepted=Count(
                "id",
                filter=Q(status="accepted"),
            ),

            rejected=Count(
                "id",
                filter=Q(status="rejected"),
            ),
        )

        recent_jobs = (
            jobs
            .order_by("-created_at")[:5]
        )

        recent_jobs_data = [
            {
                "id": job.id,
                "title": job.title,
                "company": job.company,
                "applications_count": job.applications_count,
                "is_active": job.is_active,
                "created_at": job.created_at,
            }
            for job in recent_jobs
        ]

        return Response(
            {
                **job_stats,
                **app_stats,
                "recent_jobs": recent_jobs_data,
            }
        )