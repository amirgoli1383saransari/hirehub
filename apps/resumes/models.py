from django.db import models

from apps.accounts.models import User


class Resume(models.Model):
    class EmploymentStatus(models.TextChoices):
        OPEN_TO_WORK = "open", "Open to Work"
        EMPLOYED = "employed", "Employed"
        FREELANCER = "freelancer", "Freelancer"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="resume",
    )

    title = models.CharField(max_length=255)

    summary = models.TextField(
        blank=True,
    )

    employment_status = models.CharField(
        max_length=20,
        choices=EmploymentStatus.choices,
        default=EmploymentStatus.OPEN_TO_WORK,
    )

    years_of_experience = models.PositiveIntegerField(
        default=0,
    )

    expected_salary = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    resume_file = models.FileField(
        upload_to="resumes/",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.user.email} Resume"
    
    
class Skill(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="skills",
    )

    name = models.CharField(max_length=100)

    level = models.CharField(
        max_length=20,
        choices=[
            ("beginner", "Beginner"),
            ("intermediate", "Intermediate"),
            ("advanced", "Advanced"),
            ("expert", "Expert"),
        ],
        default="beginner",
    )

    class Meta:
        unique_together = ("resume", "name")

    def __str__(self):
        return self.name
    

class Experience(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="experiences",
    )

    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    start_date = models.DateField()
    end_date = models.DateField(
        null=True,
        blank=True,
    )

    currently_working = models.BooleanField(default=False)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.position} @ {self.company}"
    

class Education(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="educations",
    )

    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=150)

    start_date = models.DateField()
    end_date = models.DateField(
        blank=True,
        null=True,
    )

    currently_studying = models.BooleanField(
        default=False,
    )

    grade = models.CharField(
        max_length=30,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.degree} - {self.institution}"