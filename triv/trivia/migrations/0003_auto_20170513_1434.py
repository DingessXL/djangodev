# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 19:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0002_auto_20170511_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='used',
        ),
    ]
