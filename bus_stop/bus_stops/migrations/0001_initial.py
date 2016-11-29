# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_id', models.CharField(max_length=256)),
                ('street', models.CharField(max_length=256)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='stop',
            unique_together=set([('stop_id', 'lat', 'lng')]),
        ),
    ]