"""
<-->.
"""

# Python modules
from rest_framework.permissions import BasePermission, SAFE_METHODS


# 3rd party Modules
# -N/A

# Project Imports
# -N/A

# Global vars
# -N/A


class UserProfilePermission(BasePermission):
    """
    Class to mange the user profiles.
    """

    def has_object_permission(self, request, view, obj):
        """
        Method to check if an object is editing itself or trying to edit some
        other objects.
        Args:
            request:
            view:
            obj:

        Returns:

        """
        if request.method in SAFE_METHODS:
            return True
        return obj.id == request.user.id
