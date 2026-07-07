from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.models import User, Profile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        help_text="Password must contain at least 8 characters.",
    )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "password",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        help_text="Registered email address."
    )

    password = serializers.CharField(
        write_only=True,
        help_text="Account password."
    )

    def validate(self, attrs):
        email = attrs["email"]
        password = attrs["password"]

        user = authenticate(
            username=email,
            password=password,
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid email or password."
            )

        refresh = RefreshToken.for_user(user)

        return {
            "user": {
                "id": user.id,
                "email": user.email,
                "username": user.username,
            },
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        source="user.email",
        read_only=True,
    )

    username = serializers.CharField(
        source="user.username",
        read_only=True,
    )

    class Meta:
        model = Profile
        fields = (
            "email",
            "username",
            "full_name",
            "phone",
            "bio",
            "city",
            "country",
            "linkedin",
            "github",
            "website",
            "avatar",
        )


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "full_name",
            "phone",
            "bio",
            "city",
            "country",
            "linkedin",
            "github",
            "website",
            "avatar",
        )

        extra_kwargs = {
            "full_name": {
                "help_text": "Your full name."
            },
            "phone": {
                "help_text": "Phone number."
            },
            "bio": {
                "help_text": "Short biography."
            },
            "city": {
                "help_text": "Current city."
            },
            "country": {
                "help_text": "Country."
            },
            "linkedin": {
                "help_text": "LinkedIn profile URL."
            },
            "github": {
                "help_text": "GitHub profile URL."
            },
            "website": {
                "help_text": "Personal website."
            },
            "avatar": {
                "help_text": "Profile image."
            },
        }