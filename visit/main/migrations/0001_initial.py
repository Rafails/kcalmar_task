# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hourBegin', models.CharField(max_length=255)),
                ('hourEnd', models.CharField(max_length=255)),
                ('day', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Nutritionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('fullname', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='meetings',
            name='nutritionist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Nutritionist'),
        ),
    ]