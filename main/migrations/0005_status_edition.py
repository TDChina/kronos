# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-24 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171224_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='edition',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='main.Edition'),
        ),
    ]