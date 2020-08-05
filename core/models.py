from django.contrib.auth.models import AbstractUser
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    ruc = models.CharField(max_length=11, blank=False, null=False)
    address = models.CharField(max_length=300, blank=True, null=False)
    phone_number = models.CharField(max_length=9, blank=True, null=False)

    def __str__(self):
        return self.name


class User(AbstractUser):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.get_full_name()
