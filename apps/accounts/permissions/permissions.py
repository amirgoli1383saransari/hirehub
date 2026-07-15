from rest_framework.permissions import BasePermission
from apps.accounts.models import User

class IsEmployer(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.EMPLOYER
        )

class IsApplicant(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.APPLICANT
        )


class IsJobOwner(BasePermission):
    """
    Only the owner of a job can edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user