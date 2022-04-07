from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager


class User(AbstractUser):
    username_validator = None
    username = None
    email = None
    national_code = models.CharField(max_length=10, unique=True, verbose_name='کد ملی')
    phone_number = models.CharField(max_length=12, verbose_name='شماره تلفن')
    USERNAME_FIELD = 'national_code'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()
