from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True
    
    create_timestamp = models.DateTimeField(auto_now_add=True)


class User(AbstractUser):
    pass


# Abstract inheritance example
class Product(BaseModel):
    pass


# One2One inheritance example
class Student(User):
    grade = models.IntegerField(default=0)


# Proxy inheritance example: 
class Teacher(User):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.first_name = "Prof. " + self.first_name
        return super().save(*args, **kwargs)

    def get_first_name(self):
        return self.first_name.upper()
    
    def __str__(self):
        return f"{self.username}, {self.first_name}"
    