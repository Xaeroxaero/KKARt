# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 16:29
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlighted', models.TextField(default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('image_source', models.ImageField(default='', upload_to='products/images/')),
                ('metod',
                 models.CharField(choices=[(1, 'akryl'), (2, 'olejna'), (3, 'akwarela')], default='', max_length=100)),
                ('price', models.CharField(blank=True, default='', max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products',
                                            to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
