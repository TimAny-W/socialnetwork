from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email,  password=None, first_name=None, last_name=None, img=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name
        user.img = img
        user.set_password(password)  # change password to hash
        # user.profile_picture = profile_picture
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, first_name=None, last_name=None, img=None):
        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return user


class CustomUser(AbstractUser):
    """Custom user class
       added email field
       added first name fiedls
       added last name fields
    """
    username = models.CharField('admin',default='admin',max_length=25)
    email = models.EmailField('Email address', unique=True, null=False)
    img = models.ImageField('Avatar', unique=False, default='user/default_avatar.png',upload_to=f'user/{email}/',)

    first_name = models.CharField('First name',unique=False,null=False,max_length=25)
    last_name = models.CharField('Last name',unique=False,null=False,max_length=25)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

