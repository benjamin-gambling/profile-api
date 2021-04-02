from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id or request.user.is_superuser


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update own status"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update their OWN status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id or request.user.is_superuser
