from rest_framework.permissions import BasePermission, SAFE_METHODS


def is_manager(request):
    return request.user.is_authenticated and request.user.is_manager


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return is_manager(request)


class IsManagerOrReadonly(BasePermission):
    def has_permission(self, request, view):
        return True if request.method in SAFE_METHODS else is_manager(request)
