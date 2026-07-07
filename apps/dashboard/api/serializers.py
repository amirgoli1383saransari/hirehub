from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):
    # Jobs
    total_jobs = serializers.IntegerField()
    active_jobs = serializers.IntegerField()
    closed_jobs = serializers.IntegerField()

    # Applications
    total_applications = serializers.IntegerField()

    pending = serializers.IntegerField()
    under_review = serializers.IntegerField()
    interview = serializers.IntegerField()
    accepted = serializers.IntegerField()
    rejected = serializers.IntegerField()

    # Recent Data
    recent_jobs = serializers.ListField()
    recent_applications = serializers.ListField()