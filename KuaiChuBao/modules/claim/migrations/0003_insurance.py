# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('claim', '0002_auto_20170911_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('obligatory', models.BooleanField()),
                ('tax', models.BooleanField()),
                ('loss', models.BooleanField()),
                ('third_party', models.IntegerField(default=0, choices=[(0, '1.1\u4e07\u5143'), (1, '2.2\u4e07\u5143'), (2, '3.3\u4e07\u5143'), (3, '4.5\u4e07\u5143'), (4, '5.1\u4e07\u5143')])),
                ('people_in_car', models.IntegerField(default=0, choices=[(0, '1.1\u4e07\u5143'), (1, '2.2\u4e07\u5143'), (2, '3.3\u4e07\u5143'), (3, '4.5\u4e07\u5143'), (4, '5.1\u4e07\u5143')])),
                ('stolen_insurance', models.BooleanField()),
                ('single_glass_broken', models.BooleanField()),
                ('natural_loss', models.BooleanField()),
                ('new_add_equip', models.BooleanField()),
                ('scratch', models.BooleanField()),
                ('engine_water', models.BooleanField()),
                ('while_repair', models.BooleanField()),
                ('cargo', models.BooleanField()),
                ('mental_loss', models.BooleanField()),
                ('frachise', models.BooleanField()),
                ('third_party_missing', models.BooleanField()),
                ('assign_repair', models.BooleanField()),
                ('insurance_company', models.IntegerField(default=0, choices=[(0, '\u4eba\u4fdd\u8d22\u9669'), (1, '\u5e73\u5b89\u8d22\u9669'), (2, '\u592a\u4fdd\u8d22\u9669'), (3, '\u9633\u5149\u8d22\u9669'), (4, '\u5927\u5730\u8d22\u9669'), (5, '\u56fd\u5bff\u8d22\u9669'), (6, '\u534e\u5b89\u8d22\u9669'), (7, '\u9f0e\u548c\u8d22\u9669'), (8, '\u5b89\u8bda\u8d22\u9669'), (9, '\u9526\u6cf0\u8d22\u9669'), (10, '\u6c38\u8bda\u8d22\u9669'), (11, '\u56fd\u5143\u8d22\u9669'), (12, '\u6c38\u5b89\u8d22\u9669')])),
                ('claim', models.ForeignKey(related_name='insurance_details', to='claim.Claim')),
            ],
        ),
    ]
