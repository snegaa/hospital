from django.db import models

# Create your models here.


class People(models.Model):
    number = models.IntegerField()
    seria = models.IntegerField()
    fam = models.CharField(max_length=30)
    imya = models.CharField(max_length=30)
    otch = models.CharField(max_length=30)
    login = models.IntegerField()
    password = models.IntegerField()

