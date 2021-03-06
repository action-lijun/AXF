# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-01-13 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AxfUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('icon', models.ImageField(upload_to='icons')),
                ('active', models.BooleanField(default=False)),
                ('token', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'axfuser',
            },
        ),
    ]
