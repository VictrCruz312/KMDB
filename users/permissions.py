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


class IsAdmOrCritic(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return request.user.is_critic or request.user.is_staff
        return False
