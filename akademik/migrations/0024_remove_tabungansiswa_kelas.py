# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-31 02:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0023_tabungansiswa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabungansiswa',
            name='Kelas',
        ),
    ]