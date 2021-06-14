# from django.conf import settings
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
#
# from .managers import CustomUserManager
#
#
# # Create your models here.
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=False, verbose_name='active')
#     is_client = models.BooleanField(default=False, verbose_name='client')
#     is_staff = models.BooleanField(default=False, verbose_name='staff')
#     date_joined = models.DateTimeField(auto_now_add=True, verbose_name='date joined')
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = CustomUserManager()
#
#     class Meta:
#         db_table = 'usr'
#
#
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
