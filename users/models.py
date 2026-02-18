from django.db import models
from django.contrib.auth.models import AbstractUser

from users.model_managers import UserManager


class User(AbstractUser):
    username = None
    
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField("first name", max_length=150, blank=False)
    last_name = models.CharField("last name", max_length=150, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email