# Generated by Django 2.1.5 on 2019-01-29 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_stock_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='ticker',
        ),
    ]
