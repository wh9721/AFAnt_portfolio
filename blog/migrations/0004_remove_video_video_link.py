# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 18:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_video_video_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_link',
        ),
    ]