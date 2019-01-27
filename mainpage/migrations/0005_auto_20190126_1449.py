# Generated by Django 2.1.5 on 2019-01-26 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_auto_20190123_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='latest_spread',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock_info',
            name='latest_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stock_price',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
