# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_dev'),
    ]

    operations = [
        migrations.AddField(
            model_name='dev',
            name='dev_summary',
            field=models.TextField(default='프로젝트 요약을 작성해야 합니다.'),
        ),
    ]
