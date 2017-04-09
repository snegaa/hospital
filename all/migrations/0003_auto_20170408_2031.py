# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all', '0002_auto_20170408_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vrach',
            name='price_second',
            field=models.IntegerField(default=0, verbose_name='Цена повторного приема'),
        ),
        migrations.AlterUniqueTogether(
            name='people',
            unique_together=set([('number_pasport', 'seria_pasport')]),
        ),
    ]
