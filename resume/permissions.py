from rest_framework.permissions import BasePermission


class IsLoggedInAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.session.get("admin_id"))