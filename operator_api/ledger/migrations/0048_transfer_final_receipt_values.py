# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-03-12 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0047_transfer_sender_finalization_aggregate'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='final_receipt_values',
            field=models.CharField(blank=True, max_length=2560, null=True),
        ),
    ]
