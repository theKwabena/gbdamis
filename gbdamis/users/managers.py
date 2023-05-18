import unicodedata

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):

    def normalize_username(cls, username):
        return (
            unicodedata.normalize("NFKC", username)
            if isinstance(username, str)
            else username
        )
    
    def _create_user(self, username, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            username=self.normalize_username(username),
            email=email,
            **extra_fields
        )

        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        Creates and saves a user with the given email and password.
        """

        extra_fields.setdefault("admin", False)
        return self._create_user(username, email, password, **extra_fields)
        # user = self._create_user(
        #     email,
        #     password=password,
        # )
        # user.staff = True
        # user.save(using=self._db)
        # return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given username and password.
        """
        extra_fields.setdefault("admin", True)
        extra_fields.setdefault("is_staff", True)
        # extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("admin") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        # if extra_fields.get("is_superuser") is not True:
        #     raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)
        # user = self.create_user(
        #     email,
        #     password=password,
        # )
        # user.staff = True
        # user.admin = True
        # user.save(using=self._db)
        # return user

