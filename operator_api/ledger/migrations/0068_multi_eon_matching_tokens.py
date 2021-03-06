# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-09-12 21:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0067_multi_eon_matching_remove'),
    ]

    operations = [
        migrations.AddField(
            model_name='matching',
            name='left_token',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='left_token', to='ledger.Token'),
        ),
        migrations.AddField(
            model_name='matching',
            name='right_token',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='right_token', to='ledger.Token'),
        ),
    ]
