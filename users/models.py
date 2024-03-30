from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    class Gender(models.TextChoices):
        MAN = 'Man'
        WOMAN = 'Woman'

    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = models.CharField(max_length=31)
    last_name = models.CharField(max_length=31)
    phone_number = models.CharField(max_length=7)
    gender = models.CharField(max_length=31, choices=Gender.choices, default=Gender.MAN)
    age = models.PositiveIntegerField(default=1)




