from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/accounts/", include("apps.accounts.api.urls")),

    path(
        "api/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),

    path(
        "api/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    path("api/resume/", include("apps.resumes.api.urls")),

    path("api/jobs/", include("apps.jobs.api.urls")),

    path(
    "api/applications/",
    include("apps.applications.api.urls"),
    ),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),

    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),

    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("api/dashboard/", include("apps.dashboard.api.urls")),

    path(
    "api/notifications/",
    include("apps.notifications.api.urls"),
    ),

    path(
    "api/bookmarks/",
    include("apps.bookmarks.api.urls"),
    ),
]
