from rest_framework import permissions

class IsAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
    
class IsAdminUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.user_type=='admin'

class IsViewerUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.user_type=='viewer' 