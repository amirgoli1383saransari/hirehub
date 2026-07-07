from rest_framework.permissions import BasePermission


class IsJobOwner(BasePermission):
    """
    Allows access only to the owner of the job.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user