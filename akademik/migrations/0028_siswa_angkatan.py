# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-02 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0027_remove_siswa_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='siswa',
            name='Angkatan',
            field=models.CharField(choices=[('Ganjil 18/19', 'Ganjil Tahun 2018/2019'), ('Genap 18/19', 'Genap Tahun 2018/2019')], max_length=15, null=True),
        ),
    ]
