from django.db import models

# Create your models here.


class Dolg(models.Model):
    speshion = models.CharField(max_length=50, verbose_name='Специальность')


class Vrach(models.Model):
    dolg = models.ForeignKey(Dolg, verbose_name='Должность')


class Bolnoy(models.Model):
    e_mail = models.EmailField()


class History(models.Model):
    date = models.DateField()
    zhalo = models.TextField(max_length=500, verbose_name='Жалобы')
    diagnoz = models.TextField(max_length=500, verbose_name='Диагноз')


class Smena(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    time = models.IntegerField()


class Zapis(models.Model):
    kabinet = models.IntegerField()
    p = models.ForeignKey(Bolnoy)
    v = models.ForeignKey(Vrach)
    talon = models.ForeignKey(Smena)





