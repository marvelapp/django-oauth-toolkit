# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-16 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0004_auto_20160525_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='pkce_code',
            field=models.TextField(null=True),
        ),
    ]
