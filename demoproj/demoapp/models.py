from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class Book(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    author =  models.CharField(max_length=200, null=True, blank=True)
    authors =  models.CharField(max_length=200, null=True, blank=True)
    isbn13 =  models.PositiveBigIntegerField( null=True, blank=True)
    isbn10 =  models.CharField(max_length=11, null=True, blank=True)
    price =  models.CharField(max_length=11, null=True, blank=True)
    publisher =  models.CharField(max_length=200, null=True, blank=True)
    pubyear =  models.PositiveIntegerField(validators=[MinValueValidator(1000), MaxValueValidator(datetime.now().year)],help_text="Use the following format: <YYYY>")
    subjects =  models.CharField(max_length=200, null=True, blank=True)
    lexile =  models.CharField(max_length=200, null=True, blank=True)
    pages =  models.CharField(max_length=200, null=True, blank=True)
    dimensions =  models.CharField(max_length=200, null=True, blank=True)      
    	
    def __str__(self):
        return self.title


#33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []