# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-10-21 18:50
from __future__ import unicode_literals

from django.db import migrations
import osf.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0190_auto_20191021_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstractnode',
            name='external_registered_date',
            field=osf.utils.fields.NonNaiveDateTimeField(blank=True, null=True),
        ),
    ]
