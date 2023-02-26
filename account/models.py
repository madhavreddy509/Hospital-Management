from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_patient= models.BooleanField('Is admin', default=False)
    is_doctor = models.BooleanField('Is customer', default=False)
    