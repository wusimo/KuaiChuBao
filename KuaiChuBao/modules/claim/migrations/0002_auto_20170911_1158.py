# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('claim', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='company',
            field=models.ForeignKey(related_name='claims', to='claim.InsuranceCompany', null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='plate',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='time',
            field=models.DateTimeField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='user',
            field=models.ForeignKey(related_name='claims', to='claim.UserInfo', null=True),
        ),
    ]
