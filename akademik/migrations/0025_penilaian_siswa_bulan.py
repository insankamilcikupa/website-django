# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-02 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0024_remove_tabungansiswa_kelas'),
    ]

    operations = [
        migrations.AddField(
            model_name='penilaian_siswa',
            name='Bulan',
            field=models.CharField(choices=[('Jan', 'Januari'), ('Feb', 'Februari'), ('Mar', 'Maret'), ('Apr', 'April'), ('Mei', 'Mei'), ('Jun', 'Juni'), ('Jul', 'Juli'), ('Agus', 'Agustus'), ('Sept', 'September'), ('Okt', 'Oktober'), ('Nov', 'November'), ('Des', 'Desember')], max_length=15, null=True),
        ),
    ]
