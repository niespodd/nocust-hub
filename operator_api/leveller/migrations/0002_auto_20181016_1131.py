# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-16 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0044_auto_20180930_1027'),
        ('leveller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='transfer',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ledger.Transfer'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='beginning',
            field=models.DateTimeField(),
        ),
    ]