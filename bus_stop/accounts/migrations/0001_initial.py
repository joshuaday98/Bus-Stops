# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-20 00:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateTimeField()),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('first_name', models.CharField(max_length=999)),
                ('last_name', models.CharField(max_length=999)),
                ('gender', models.CharField(max_length=999)),
                ('home_str', models.CharField(max_length=999)),
                ('home_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('home_lng', models.DecimalField(decimal_places=6, max_digits=9)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
