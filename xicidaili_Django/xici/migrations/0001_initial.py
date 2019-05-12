# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DaiLi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('country', models.CharField(max_length=50)),
                ('ipaddress', models.CharField(max_length=50)),
                ('port', models.IntegerField()),
                ('serveraddr', models.CharField(max_length=20)),
                ('isanonymous', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=20)),
                ('alivetime', models.CharField(max_length=20)),
                ('verifictiontime', models.CharField(max_length=20)),
            ],
        ),
    ]
