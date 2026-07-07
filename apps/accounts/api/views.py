from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)

from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    ProfileSerializer,
    ProfileUpdateSerializer,
)


@extend_schema(
    summary="Register",
    description="Create a new user account.",
    tags=["Authentication"],
)
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


@extend_schema(
    summary="Login",
    description="Authenticate a user and return JWT access and refresh tokens.",
    tags=["Authentication"],
    request=LoginSerializer,
    responses={
        200: OpenApiResponse(description="Login successful."),
        400: OpenApiResponse(description="Invalid email or password."),
    },
    examples=[
        OpenApiExample(
            "Login Example",
            value={
                "email": "test@example.com",
                "password": "12345678",
            },
            request_only=True,
        ),
    ],
)
class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            serializer.validated_data,
            status=status.HTTP_200_OK,
        )


@extend_schema(
    summary="Current User Profile",
    description="Retrieve or update the authenticated user's profile.",
    tags=["Profile"],
)
class MeView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProfileSerializer
        return ProfileUpdateSerializer

    def get_object(self):
        return self.request.user.profile
    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Logged out successfully"})
        except Exception:
            return Response({"detail": "Invalid token"}, status=400)