from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Permission
from django.db import models
from model_utils.models import TimeStampedModel

from applications.users.managers import UserManager


class Rol(models.Model):
    rol = models.CharField('Rol', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.rol


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, blank=True, null=True)
    user_permissions = models.ManyToManyField(Permission)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', ]

    objects = UserManager()

    class Meta:
        db_table = 'auth_user'

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
