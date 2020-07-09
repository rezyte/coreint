# Generated by Django 3.0.7 on 2020-07-07 08:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0009_auto_20200706_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 7, 8, 48, 1, 143833, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='telephone_number',
            field=models.CharField(max_length=20),
        ),
    ]
