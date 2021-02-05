from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, email, phone, organization, address, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            organization=organization,
            address=address,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, organization, address, email, password):
        user = self.create_user(
            email,
            phone=phone,
            organization=organization,
            address=address,
            password=password,
        )
        user.is_organization = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    phone=models.CharField(max_length=100)
    organization=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    
    is_organization = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'organization', 'address',]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin