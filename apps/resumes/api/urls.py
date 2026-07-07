from django.urls import path
from .views import (
    ResumeView,
    SkillListCreateView,
    SkillDetailView,
    ExperienceListCreateView,
    ExperienceDetailView,
    EducationListCreateView,
    EducationDetailView,
)

urlpatterns = [
    path("me/", ResumeView.as_view()),
    path("skills/", SkillListCreateView.as_view()),
    path("skills/<int:pk>/", SkillDetailView.as_view()),
    path(
    "experiences/",
    ExperienceListCreateView.as_view(),
),

path(
    "experiences/<int:pk>/",
    ExperienceDetailView.as_view(),
),

path(
    "educations/",
    EducationListCreateView.as_view(),
    name="education-list",
),

path(
    "educations/<int:pk>/",
    EducationDetailView.as_view(),
    name="education-detail",
),
]