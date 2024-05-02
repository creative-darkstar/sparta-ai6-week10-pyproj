from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class UserInfo(AbstractUser):
    email = models.EmailField(unique=True)
    # email = models.EmailField(unique=True, validators=[RegexValidator])
    nickname = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField(default=date.today)
    introduction = models.TextField(null=True)

    SEX_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )

    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        null=True,
    )
