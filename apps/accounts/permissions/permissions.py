from rest_framework.permissions import BasePermission


class IsEmployer(BasePermission):
    """
    Allows access only to employers.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "employer"
        )


class IsApplicant(BasePermission):
    """
    Allows access only to applicants.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "applicant"
        )


class IsJobOwner(BasePermission):
    """
    Only the owner of a job can edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user