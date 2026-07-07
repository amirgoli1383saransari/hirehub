from rest_framework import serializers

from apps.jobs.models import Job


class JobSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Job

        fields = (
            "id",
            "owner",
            "title",
            "company",
            "location",
            "description",
            "salary_min",
            "salary_max",
            "job_type",
            "experience_level",
            "is_active",
            "created_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "owner",
            "created_at",
            "updated_at",
        )

    def validate(self, attrs):
        salary_min = attrs.get("salary_min")
        salary_max = attrs.get("salary_max")

        if (
            salary_min is not None
            and salary_max is not None
            and salary_min > salary_max
        ):
            raise serializers.ValidationError(
                {
                    "salary_max":
                    "salary_max must be greater than salary_min."
                }
            )

        return attrs