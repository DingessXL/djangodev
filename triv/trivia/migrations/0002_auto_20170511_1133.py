# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='subcategory',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]