# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-16 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leveller', '0002_auto_20181016_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='beginning',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
