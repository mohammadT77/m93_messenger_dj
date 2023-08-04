from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# class BaseModel(models.Model):
#     ...
#     pass

class User(AbstractUser):
    pass