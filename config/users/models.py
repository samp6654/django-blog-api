from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'user'
    MANAGER = 'manager'

    ROLE_CHOICES = (
        (USER, 'User'),
        (MANAGER, 'Manager'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=USER
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
