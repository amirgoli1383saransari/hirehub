from rest_framework import serializers
from apps.resumes.models import Resume
from apps.resumes.models import Skill
from apps.resumes.models import Experience
from apps.resumes.models import Education




class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = (
            "id",
            "name",
            "level",
        )

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        
        fields = (
             "id",
             "company",
             "position",
             "start_date",
             "end_date",
             "currently_working",
             "description",
             "created_at",
             )
        read_only_fields = (
            "id",
            "created_at",
            )


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            "id",
            "institution",
            "degree",
            "field_of_study",
            "start_date",
            "end_date",
            "currently_studying",
            "grade",
            "description",
            "created_at",
        )

        read_only_fields = (
            "id",
            "created_at",
        )


class ResumeSerializer(serializers.ModelSerializer):

    skills = SkillSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    educations = EducationSerializer(many=True, read_only=True)


    class Meta:
        model = Resume
        exclude = (
            "user",
        )