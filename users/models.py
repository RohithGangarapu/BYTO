from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        # Set default values for required fields
        extra_fields.setdefault('user_type', 'partner')  # or any default you prefer
        extra_fields.setdefault('firstname', 'Admin')
        extra_fields.setdefault('lastname', 'User')
        extra_fields.setdefault('phone', 0)
        
        return self.create_user(email, password, **extra_fields)
class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('partner', 'Partner'),
        ('customer', 'Customer'),
    )
    photo=models.ImageField(upload_to='./userimages',blank=True,default=None)
    firstname = models.CharField(max_length=20, blank=True)  # Changed from default=None
    lastname = models.CharField(max_length=25, blank=True)   # Changed from default=None
    email = models.EmailField(unique=True)
    phone = models.IntegerField(blank=True, null=True)       # Made nullable
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='partner')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Empty list means only email and password are required for superuser

    objects = CustomUserManager()

    def __str__(self):
        return self.email