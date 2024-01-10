from rest_framework.permissions import BasePermission

class MyCustomPemissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user and request.user.is_superuser
        else:
            return True
