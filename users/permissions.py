from rest_framework.permissions import BasePermission, SAFE_METHODS
import ipdb


class IsAdmForListing(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.is_superuser
        return True


class IsAdmOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_superuser
