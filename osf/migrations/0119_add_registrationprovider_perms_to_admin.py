# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-10 17:34
from __future__ import unicode_literals

from django.db import migrations


def noop(*args):
    # This migration used to update admin permissions
    # This is now handled by the post_migrate signal
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0118_auto_20180706_1127'),
    ]

    operations = [
        migrations.RunPython(noop, noop),
    ]