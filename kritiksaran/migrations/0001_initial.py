# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-03 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KritikSaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isi', models.TextField()),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tabel Kritik dan Saran',
                'verbose_name_plural': 'Tabel Kritik dan Saran',
            },
        ),
    ]
