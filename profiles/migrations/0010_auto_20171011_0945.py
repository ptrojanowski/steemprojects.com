# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-11 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0009_auto_20170908_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created',
                 django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified',
                 django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('type', models.CharField(choices=[('STEEM', 'Steem'), ('GITHUB', 'Github')], max_length=15,
                                          verbose_name='Type')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Account confirmed')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([('name', 'type')]),
        ),
    ]
