from django.contrib import admin

from .models import Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "title",
        "employment_status",
        "years_of_experience",
    )

    search_fields = (
        "user__email",
        "title",
    )