from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Добавляем дополнительные поля, если необходимо
    age = models.PositiveIntegerField(null=True, blank=True)
