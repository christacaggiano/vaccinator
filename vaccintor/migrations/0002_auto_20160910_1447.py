# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 18:47
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccintor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine',
            name='age_days',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaccine',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaccine',
            name='description',
            field=models.TextField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaccine',
            name='subsidized',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
