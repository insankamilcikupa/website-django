# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-16 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0002_auto_20190716_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pengembangan',
            fields=[
                ('Kode_Pengembangan', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('Judul_Pengembangan', models.CharField(max_length=50)),
            ],
        ),
    ]
