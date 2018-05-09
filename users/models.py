from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from bookings.models import Bookings


class Manager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email Must be Set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff')is not True:
            raise ValueError('Superuser Must have is_staff = True')
        if extra_fields.get('is_superuser')is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)


class User:

    bookingList = [Bookings]


class Customer(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
    password = models.TextField(max_length=100, default="")
    first_name = models.CharField(blank=True, max_length=40)
    last_name = models.CharField(blank=True, max_length=40)
    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the user can log into this site.')
    Address_Line_1 = models.CharField(blank=True, max_length=255)
    Address_Line_2 = models.CharField(blank=True, max_length=255)
    town = models.CharField(blank=True, max_length=50)
    postCode = models.CharField(blank=True, max_length=8)
    PhoneNumber = models.CharField(blank=True, max_length=15)
    homePhone = models.CharField(blank=True, max_length=15)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = Manager()

    def get_username(self):
        return self.email
