from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserPeople(AbstractUser):
    number = models.IntegerField(null=True)
    seria = models.IntegerField(null=True)
    middleName = models.CharField(max_length=30)


class Role:
    name = models.TextField(max_length=20)
    description = models.TextField(max_length=20)
    key_many_users_people = models.ManyToManyField(UserPeople)




