from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    is_active = models.BooleanField(default=False, verbose_name='active')
    is_client = models.BooleanField(default=False, verbose_name='client')
    is_staff = models.BooleanField(default=False, verbose_name='staff')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='date joined')

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    class Meta:
        db_table = 'usr'
