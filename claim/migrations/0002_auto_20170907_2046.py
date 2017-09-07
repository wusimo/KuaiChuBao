# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('claim', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='claim',
            field=models.ForeignKey(to='claim.Claim', null=True),
        ),
    ]
