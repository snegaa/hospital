from django.db import models

# Create your models here.


class People(models.Model):
    number_pasport = models.IntegerField(verbose_name='Номер паспорта')
    seria_pasport = models.IntegerField(verbose_name='Серия паспорта')
    familia = models.TextField(max_length=20, verbose_name='Фамилия')
    imya = models.TextField(max_length=20, verbose_name='Имя')
    otchestvo = models.TextField(max_length=20, verbose_name = 'Отчество')
    parol = models.IntegerField(verbose_name='Пароль')

    class Meta:
        unique_together = ('number_pasport', 'seria_pasport')

    def __str__(self):
        return '{0} {1}'.format(self.imya, self.familia)


class Dolzhnost(models.Model):
    position = models.CharField(max_length=50, verbose_name='Должность')

    def __str__(self):
        return self.position


class Vrach(models.Model):
    FK_People = models.ForeignKey(People)
    FK_position = models.ForeignKey(Dolzhnost)
    price_ferst = models.IntegerField(default=0, verbose_name='Цена первичного приема')
    price_second = models.IntegerField(default=0, verbose_name='Цена повторного приема')

    def __str__(self):
        return '{0}, {1}'.format(str(self.FK_People), str(self.FK_position))


class Bolnoy(models.Model):
    FK_People = models.ForeignKey(People)
    e_mail = models.EmailField()



class History(models.Model):
    date = models.DateField()
    complaint = models.TextField(max_length=500, verbose_name='Жалобы')
    diagnosis = models.TextField(max_length=500, verbose_name='Диагноз')


class Smena(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    time = models.IntegerField()


class Zapis(models.Model):
    kabinet = models.IntegerField()
    FK_People = models.ForeignKey(Bolnoy)
    FK_Vrach = models.ForeignKey(Vrach)
    talon = models.ForeignKey(Smena)









