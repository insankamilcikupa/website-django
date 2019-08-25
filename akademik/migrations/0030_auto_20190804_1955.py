# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-04 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0029_auto_20190802_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penilaian_siswa',
            name='Bulan',
            field=models.CharField(choices=[('Jan 1', 'Januari M1'), ('Jan 2', 'Januari M2'), ('Jan 3', 'Januari M3'), ('Jan 4', 'Januari M4'), ('Feb 1', 'Februari M1'), ('Feb 2', 'Februari M2'), ('Feb 3', 'Februari M3'), ('Feb 4', 'Februari M4'), ('Mar 1', 'Maret M1'), ('Mar 2', 'Maret M2'), ('Mar 3', 'Maret M3'), ('Mar 4', 'Maret M4'), ('Apr 1', 'April M1'), ('Apr 2', 'April M2'), ('Apr 3', 'April M3'), ('Apr 4', 'April M4'), ('Mei 1', 'Mei M1'), ('Mei 2', 'Mei M2'), ('Mei 3', 'Mei M3'), ('Mei 4', 'Mei M4'), ('Jun 1', 'Juni M1'), ('Jun 2', 'Juni M2'), ('Jun 3', 'Juni M3'), ('Jun 4', 'Juni M4'), ('Jul 1', 'Juli M1'), ('Jul 2', 'Juli M2'), ('Jul 3', 'Juli M3'), ('Jul 4', 'Juli M4'), ('Agus 1', 'Agustus M1'), ('Agus 2', 'Agustus M2'), ('Agus 3', 'Agustus M3'), ('Agus 4', 'Agustus M4'), ('Sept 1', 'September M1'), ('Sept 2', 'September M2'), ('Sept 3', 'September M3'), ('Sept 4', 'September M4'), ('Okt 1', 'Oktober M1'), ('Okt 2', 'Oktober M2'), ('Okt 3', 'Oktober M3'), ('Okt 4', 'Oktober M4'), ('Nov 1', 'November M1'), ('Nov 2', 'November M2'), ('Nov 3', 'November M3'), ('Nov 4', 'November M4'), ('Des 1', 'Desember M1'), ('Des 2', 'Desember M2'), ('Des 3', 'Desember M3'), ('Des 4', 'Desember M4')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='penilaian_siswa',
            name='Penilaian',
            field=models.CharField(choices=[('SB', 'Sangat Bisa'), ('B', 'Bisa'), ('CB', 'Cukup Bisa'), ('BB', 'Belum Bisa')], max_length=20),
        ),
    ]