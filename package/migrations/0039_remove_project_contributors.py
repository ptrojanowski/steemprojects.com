# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-12 21:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0038_auto_20171012_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='contributors',
        ),
    ]
