import django_filters

from apps.jobs.models import Job


class JobFilter(django_filters.FilterSet):
    salary_min = django_filters.NumberFilter(
        field_name="salary_min",
        lookup_expr="gte",
    )

    salary_max = django_filters.NumberFilter(
        field_name="salary_max",
        lookup_expr="lte",
    )

    class Meta:
        model = Job
        fields = (
            "location",
            "job_type",
            "experience_level",
            "is_active",
            "salary_min",
            "salary_max",
        )