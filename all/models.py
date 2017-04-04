from django.db import models

# Create your models here.

class People(models.Model):
    number_pasport = models.IntegerField(verbose_name = 'Номер паспорта')
    seria_pasport = models.IntegerField(verbose_name='Серия паспорта')
    familia = models.TextField(max_length = 20, verbose_name='Фамилия')
    imya = models.TextField(max_length = 20, verbose_name='Имя')
    otch = models.TextField(max_length = 20, verbose_name = 'Отчество')
    parol = models.IntegerField(verbose_name='Пароль')



class Dolzhnost(models.Model):
    speshion = models.CharField(max_length=50, verbose_name='Должность')


class Vrach(models.Model):
    p = models.ForeignKey(People)
    d = models.ForeignKey(Dolzhnost)


class Bolnoy(models.Model):
    p = models.ForeignKey(People)
    e_mail = models.EmailField()



class History(models.Model):
    date = models.DateField()
    zhaloby = models.TextField(max_length=500, verbose_name='Жалобы')
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









