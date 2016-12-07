from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone




# Create your models here.


class AccountUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given user must be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractUser):
    stripe_id = models.CharField(max_length=40, default='')
    subscription_end = models.DateTimeField(default=timezone.now)
    objects = AccountUserManager()


class Reservation(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=False, unique=True,
        error_messages={'required': 'Please provide your email address.',
                        'unique': 'An account with this email exist.'},)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(default=0)  # Record how often a post is seen
    telephone= models.CharField(max_length=12)
    guests= models.IntegerField()
