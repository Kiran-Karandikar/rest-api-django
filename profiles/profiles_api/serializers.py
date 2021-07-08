"""
<-->.
"""

# Python modules
from rest_framework import serializers as szs

from .models import UserProfile


# 3rd party Modules
# -N/A

# Project Imports
# -N/A

# Global vars
# -N/A


class HelloSerailzer(szs.Serializer):
    """
    Serialize to serialize the name passed to api view.
    """
    name = szs.CharField(max_length = 10)


class UserProfilerSerializer(szs.ModelSerializer):
    """
    Serializer class to handle all serialization requirements of User profile
    models.
    """

    class Meta:
        """
        Meta Class.
        """
        model = UserProfile
        fields = ("id", "names", "email", "password")
        extra_kwargs = {
                "password": {
                        "write_only": True, "style": {
                                "input_type": "password"
                        }

                }
        }

    def create(self, validated_data):
        """
        Create and return new user.
        Args:
            validated_data:

        Returns:

        """
        email = validated_data.get("email")
        name = validated_data.get("name")
        password = validated_data.get("password")

        user = UserProfile.objects.create_user(email = email, name = name,
            password = password)
        return user

    def update(self, instance, validated_data):
        """
        Updates the user profile object for required fields.
        Args:
            instance:
            validated_data:

        Returns:

        """
        password = validated_data.get("password", None)
        if password:
            instance.set_password(password)
            validated_data.pop("password")

        return super(UserProfilerSerializer, self).update(instance,
            validated_data)
