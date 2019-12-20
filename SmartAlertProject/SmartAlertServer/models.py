from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Contact(AbstractUser):
    active = models.BooleanField(("active"), default=True)
    date_added = models.DateTimeField(default=timezone.now)
    dob = models.CharField(max_length=255)
    last_login = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=255)
    terminated = models.BooleanField(("terminated"), default=False)
    is_god = models.BooleanField(("is_god"), default=False)
    api_key = models.CharField(max_length=255)
    date_updated = models.DateTimeField(default=timezone.now)
    purchase_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name