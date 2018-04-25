# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engplatform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='machinelist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddr', models.CharField(max_length=18)),
                ('netmask', models.CharField(max_length=18)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('mcmark', models.CharField(max_length=30)),
                ('mccpu', models.IntegerField(default=36)),
                ('mcmem', models.IntegerField(default=36)),
                ('mcalldisk', models.IntegerField(default=0)),
                ('mcrundisk', models.IntegerField(default=0)),
                ('mcprocessallnum', models.IntegerField(default=0)),
                ('mcprocessrunnum', models.IntegerField(default=0)),
                ('mcprocesszomnum', models.IntegerField(default=0)),
                ('mcdiskspeed', models.IntegerField(default=0)),
                ('mcnetspeed', models.IntegerField(default=0)),
            ],
        ),
    ]
