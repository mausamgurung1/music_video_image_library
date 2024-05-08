
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, default=False)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=15, default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users_groups',
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
