# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-25 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setId', models.IntegerField()),
                ('questions', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]