# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-08 19:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0002_auto_20170108_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientslist',
            old_name='weight_in_g',
            new_name='weight_for_100g',
        ),
    ]
