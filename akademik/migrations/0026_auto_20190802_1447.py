# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-02 07:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0025_penilaian_siswa_bulan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='penilaian_siswa',
            old_name='Kode_Pengembangan',
            new_name='Judul_Pengembangan',
        ),
    ]
