# Generated by Django 2.1.5 on 2019-01-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20190123_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='id',
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]