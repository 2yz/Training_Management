# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 07:53
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0014_auto_20170515_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(default='settings.MEDIA_ROOT/avatar/timg.jpg', storage=django.core.files.storage.FileSystemStorage(location=b'/Users/arlex/Documents/Python/PlanTraning/media'), upload_to='avatar'),
        ),
    ]
