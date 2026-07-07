from django.db.models import Count, Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.jobs.models import Job
from apps.applications.models import Application

from .serializers import DashboardSerializer

class ApplicantDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        applications = Application.objects.filter(
            applicant=request.user
        ).select_related("job")

        stats = applications.aggregate(
            total_applications=Count("id"),
            pending=Count("id", filter=Q(status="pending")),
            under_review=Count("id", filter=Q(status="under_review")),
            interview=Count("id", filter=Q(status="interview")),
            accepted=Count("id", filter=Q(status="accepted")),
            rejected=Count("id", filter=Q(status="rejected")),
        )

        recent_applications = applications.order_by("-created_at")[:5]

        recent_data = [
            {
                "job_id": app.job.id,
                "title": app.job.title,
                "company": app.job.company,
                "status": app.status,
                "applied_at": app.created_at,
            }
            for app in recent_applications
        ]

        data = {
            **stats,
            "recent_applications": recent_data,
        }

        return Response(data)
    
class EmployerDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        jobs = Job.objects.filter(
            owner=request.user
        )

        applications = Application.objects.filter(
            job__owner=request.user
        ).select_related("job", "applicant")

        job_stats = jobs.aggregate(
            total_jobs=Count("id"),
            active_jobs=Count("id", filter=Q(is_active=True)),
            closed_jobs=Count("id", filter=Q(is_active=False)),
        )

        app_stats = applications.aggregate(
            total_applications=Count("id"),
            pending=Count("id", filter=Q(status="pending")),
            under_review=Count("id", filter=Q(status="under_review")),
            interview=Count("id", filter=Q(status="interview")),
            accepted=Count("id", filter=Q(status="accepted")),
            rejected=Count("id", filter=Q(status="rejected")),
        )

        recent_jobs = jobs.order_by("-created_at")[:5]

        recent_jobs_data = [
            {
                "id": job.id,
                "title": job.title,
                "company": job.company,
                "applications_count": Application.objects.filter(job=job).count(),
                "is_active": job.is_active,
                "created_at": job.created_at,
            }
            for job in recent_jobs
        ]

        return Response({
            **job_stats,
            **app_stats,
            "recent_jobs": recent_jobs_data,
        })
    
