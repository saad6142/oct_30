# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-29 10:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fib_api', '0002_auto_20160907_0419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fibonacciresults',
            old_name='number',
            new_name='digits',
        ),
        migrations.RenameField(
            model_name='fibonacciresults',
            old_name='result',
            new_name='final',
        ),
        migrations.RenameField(
            model_name='fibonacciresults',
            old_name='time_taken',
            new_name='time',
        ),
        migrations.AlterModelTable(
            name='fibonacciresults',
            table='fibonacci_db',
        ),
    ]
