# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-21 12:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0033_transfer_cancelled'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfer',
            old_name='sent',
            new_name='complete',
        ),
    ]
