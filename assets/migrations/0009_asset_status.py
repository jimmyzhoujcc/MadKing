# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_software_sub_asset_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '在线'), (1, '已下线'), (2, '未知'), (3, '故障'), (4, '备用')], default=0),
        ),
    ]
