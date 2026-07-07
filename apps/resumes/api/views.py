from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.resumes.models import Resume
from .serializers import ResumeSerializer
from apps.resumes.models import Skill
from apps.resumes.models import Education
from .serializers import SkillSerializer,ExperienceSerializer,EducationSerializer


class ResumeView(generics.RetrieveUpdateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        resume, created = Resume.objects.get_or_create(
            user=self.request.user,
            defaults={
                "title": "",
            },
        )

        return resume
    


class SkillListCreateView(generics.ListCreateAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.resume.skills.all()

    def perform_create(self, serializer):
        serializer.save(
            resume=self.request.user.resume
        )


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.resume.skills.all()
    

class ExperienceListCreateView(generics.ListCreateAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.resume.experiences.all()

    def perform_create(self, serializer):
        serializer.save(
            resume=self.request.user.resume
        )


class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.resume.experiences.all()
    

class EducationListCreateView(generics.ListCreateAPIView):
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Education.objects.filter(
            resume=self.request.user.resume
        )

    def perform_create(self, serializer):
        serializer.save(
            resume=self.request.user.resume
        )


class EducationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Education.objects.filter(
            resume=self.request.user.resume
        )