# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-12-11 09:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0069_multi_eon_matching_tokens_populate'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='sell_order',
            field=models.BooleanField(default=True),
        ),
    ]
