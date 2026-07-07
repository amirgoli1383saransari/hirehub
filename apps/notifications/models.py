from django.db import models

from apps.accounts.models import User


class Notification(models.Model):
    class Type(models.TextChoices):
        APPLICATION = "application", "Application"
        STATUS_UPDATE = "status_update", "Status Update"
        MESSAGE = "message", "Message"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    title = models.CharField(max_length=255)

    message = models.TextField()

    notification_type = models.CharField(
        max_length=30,
        choices=Type.choices,
    )

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return self.title