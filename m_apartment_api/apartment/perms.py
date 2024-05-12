from rest_framework import permissions

class Owner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return super().has_permission(request, view) and (request.user.id == obj.resident.id or request.user.is_staff)

class IsStaff(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return super().has_permission(request, view) and request.user.is_staff