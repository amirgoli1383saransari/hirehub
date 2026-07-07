from rest_framework import serializers
from apps.bookmarks.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):

    job_title = serializers.ReadOnlyField(source="job.title")
    company = serializers.ReadOnlyField(source="job.company")

    class Meta:
        model = Bookmark

        fields = (
            "id",
            "job",
            "job_title",
            "company",
            "created_at",
        )

        read_only_fields = ("id", "created_at")