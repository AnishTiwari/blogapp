# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-01 13:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
