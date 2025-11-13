from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, null=True)
    phone = models.CharField(max_length=10, null=True)
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student')
    )

    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.username
