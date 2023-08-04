from typing import Any, Dict, Tuple
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

from django.db.models.query import QuerySet

# Create your models here.
class BaseManager(models.Manager):

    # TODO: implement Logical Delete here!
    
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_deleted=False)

    def archive(self):
        return super().get_queryset()


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = BaseManager()
    
    is_deleted = models.BooleanField(default=False, db_index=True, null=False, blank=False)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    delete_timestamp = models.DateTimeField(default=None, null=True, blank=True)
    modify_timestamp = models.DateTimeField(auto_now=True)

    def delete(self, **kwargs) -> Tuple[int, Dict[str, int]]:
        self.is_deleted = True
        self.delete_timestamp = datetime.now()
        self.save(using=kwargs.get("using"))


class User(AbstractUser):
    pass

# Abstract inheritance example
class Product(BaseModel):
    name = models.CharField(max_length=20)
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
    