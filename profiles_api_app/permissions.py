from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""
    #called evry time request is made
    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""
        #safe - http get unsafe - http post,put
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #check if user is trying to edit their own profile
        return obj.id == request.user.id