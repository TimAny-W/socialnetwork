from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


# Create your models here.


class CustomUser(AbstractUser):
    """Custom user class
       added email field
    """
    email = models.EmailField('Email address', unique=True, null=False)
    img = models.ImageField('Аватарка', unique=False, default='g')

    def __str__(self):
        return self.username
