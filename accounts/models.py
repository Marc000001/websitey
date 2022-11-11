

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager
from django.db import models


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, is_active=True, is_staff=False, is_admin=False, is_personel=False,
                    is_patient=False):
        if not username:
            raise ValueError("Must have Username")
        if not password:
            raise ValueError("Must have password")

        user_obj = self.model(
            username=username
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.personel = is_personel
        user_obj.patient = is_patient
        user_obj.active = is_active
        user_obj.save(using=self._db)

        return user_obj

    def create_patient(self, username, password=None):
        user = self.create_patient(
            username,
            password=password,
            is_staff=True,
            is_active=True
        )
        return user

    def create_staffuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            is_patient=True,
            is_active=True
        )
        return user

    def create_personel(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            is_personel=True,
            is_active=True
        )
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            is_staff=True,
            is_admin=True,
            is_active=True,
        )
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    personel = models.BooleanField(default=False)
    patient = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=30, null=True, blank=True)
    ward = models.CharField(max_length=30, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_personel(self):
        return self.personel

    @property
    def is_active(self):
        return self.active

    @property
    def is_patient(self):
        return self.patient


