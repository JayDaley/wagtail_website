# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-05 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0004_auto_20160315_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glossarypage',
            name='introduction',
            field=models.CharField(blank=True, help_text='The page introduction text. You can only use 511 characters.', max_length=511),
        ),
    ]