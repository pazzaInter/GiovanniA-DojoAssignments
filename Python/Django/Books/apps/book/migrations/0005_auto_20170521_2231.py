# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 05:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20170521_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book.Author'),
            preserve_default=False,
        ),
    ]