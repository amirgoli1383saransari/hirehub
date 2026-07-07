from rest_framework import serializers

from apps.applications.models import Application
from apps.jobs.models import Job
from apps.resumes.models import Resume


class ApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.ReadOnlyField(
        source="applicant.email"
    )

    job_title = serializers.ReadOnlyField(
        source="job.title"
    )

    company = serializers.ReadOnlyField(
        source="job.company"
    )

    class Meta:
        model = Application

        fields = (
            "id",
            "applicant",
            "job",
            "job_title",
            "company",
            "resume",
            "cover_letter",
            "status",
            "created_at",
        )

        read_only_fields = (
            "id",
            "applicant",
            "status",
            "created_at",
        )

    def validate(self, attrs):
        request = self.context["request"]

        applicant = request.user
        job = attrs["job"]
        resume = attrs["resume"]

        if not job.is_active:
            raise serializers.ValidationError(
                "This job is no longer accepting applications."
            )

        if job.owner == applicant:
            raise serializers.ValidationError(
                "You cannot apply for your own job."
            )

        if Application.objects.filter(
            applicant=applicant,
            job=job,
        ).exists():
            raise serializers.ValidationError(
                "You have already applied for this job."
            )

        if resume.user != applicant:
            raise serializers.ValidationError(
                "This resume does not belong to you."
                )

        return attrs

    def create(self, validated_data):
        validated_data["applicant"] = self.context["request"].user

        return super().create(validated_data)
    

class EmployerApplicationSerializer(serializers.ModelSerializer):
    applicant_email = serializers.ReadOnlyField(
        source="applicant.email"
    )

    applicant_username = serializers.ReadOnlyField(
        source="applicant.username"
    )

    resume_title = serializers.ReadOnlyField(
        source="resume.title"
    )

    class Meta:
        model = Application

        fields = (
            "id",
            "applicant_email",
            "applicant_username",
            "resume_title",
            "status",
            "cover_letter",
            "created_at",
        )

        read_only_fields = fields


class ApplicationStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ("status",)

    def validate_status(self, value):
        if value not in (
            Application.Status.UNDER_REVIEW,
            Application.Status.INTERVIEW,
            Application.Status.ACCEPTED,
            Application.Status.REJECTED,
        ):
            raise serializers.ValidationError(
                "Invalid application status."
            )

        return value