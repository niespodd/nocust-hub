# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-05 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0014_challenge_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='registration_hub_authorization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='hub_registration_signature', to='ledger.Signature'),
        ),
    ]
