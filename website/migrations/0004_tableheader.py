# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-30 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_tablerow_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
