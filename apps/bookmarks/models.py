from django.db import models
from apps.accounts.models import User
from apps.jobs.models import Job


class Bookmark(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookmarks",
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="bookmarks",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "job"],
                name="unique_bookmark",
            )
        ]

        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.email} -> {self.job.title}"