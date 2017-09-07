# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import claim.models


class Migration(migrations.Migration):

    dependencies = [
        ('claim', '0002_auto_20170907_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='claim',
            field=models.ForeignKey(to='claim.Claim', null=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to=claim.models.get_image_filename, verbose_name='image'),
        ),
    ]
