# Generated by Django 3.0.7 on 2020-07-03 06:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 3, 6, 56, 15, 510780, tzinfo=utc)),
        ),
    ]