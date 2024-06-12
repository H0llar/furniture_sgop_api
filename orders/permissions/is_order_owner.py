from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOrderOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

    def has_permission(self, request, view):
        return request.method in [*SAFE_METHODS, 'POST']
