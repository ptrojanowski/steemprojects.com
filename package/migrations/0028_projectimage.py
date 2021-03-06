# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-03 07:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import package.models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0027_auto_20170902_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('img', models.ImageField(default='None/no-img.jpg', upload_to=package.models.project_img_path)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
