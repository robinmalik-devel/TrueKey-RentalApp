from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from apps.core.models import BaseModel

indian_mobile = RegexValidator(
    r"^\+91[6-9]\d{9}$", "Enter an Indian mobile number as +91XXXXXXXXXX."
)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone, **extra_fields):
        user = self.model(phone=phone, **extra_fields)
        user.set_unusable_password()  # OTP login only
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault("role", User.Role.ADMIN)
        user = self.model(phone=phone, is_staff=True, is_superuser=True, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        TENANT = "tenant", "Tenant"
        OWNER = "owner", "Owner"
        VERIFIER = "verifier", "Verifier"
        ADMIN = "admin", "Admin"

    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        SUSPENDED = "suspended", "Suspended"
        BANNED = "banned", "Banned"

    phone = models.CharField(max_length=13, unique=True, validators=[indian_mobile])
    name = models.CharField(max_length=120, blank=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.TENANT)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    trust_level = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ()  # createsuperuser asks only for phone and password

    def __str__(self):
        return self.phone