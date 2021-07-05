"""
Docstring.
"""
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin,
)
from django.db import models


class UserProfileManger(BaseUserManager):
    """
    Class to mange the user profiles.
    """

    def create_user(self, email, name, password = None):
        """
        Create a new user with provided details.
        Args:
            email:
            name:
            password:

        Returns:

        """
        if not email:
            raise ValueError("Please provide the email address for this user")

        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        user.set_password(password)
        user.is_active = True

        # This line is to allow django support multiple databases in future.
        user.save(using = self._db)

        return user

    def create_superuser(self, email, name, password = None):
        """
        Create super user with provided details and assign super user status.
        Args:
            email:
            name:
            password:

        Returns:

        """
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        # This line is to allow django support multiple databases in future.
        user.save(using = self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Base class for custom user controls.
    """
    email = models.EmailField(unique = True, max_length = 255)
    name = models.CharField(max_length = 255)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = False)

    objects = UserProfileManger()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        """
        Return the string representation of user.
        Returns:

        """
        return self.email

    def get_full_name(self):
        """
        Get full name of user.
        Returns:

        """
        return self.name

    def get_short_name(self):
        """
        Get short name of user.
        Returns:

        """
        return self.name
