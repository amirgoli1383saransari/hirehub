from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.accounts.permissions import IsEmployer
from apps.jobs.models import Job
from apps.jobs.permissions import IsJobOwner
from apps.jobs.filters import JobFilter

from .serializers import JobSerializer


class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_class = JobFilter

    search_fields = (
        "title",
        "company",
        "description",
        "location",
    )

    ordering_fields = (
        "created_at",
        "salary_min",
        "salary_max",
        "title",
    )

    ordering = (
        "-created_at",
    )

    def get_queryset(self):
        return Job.objects.filter(is_active=True)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsEmployer()]

        return [IsAuthenticatedOrReadOnly()]


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer

    queryset = Job.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticatedOrReadOnly()]

        return [
            IsEmployer(),
            IsJobOwner(),
        ]