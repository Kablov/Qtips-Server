# Generated by Django 2.1.2 on 2018-12-05 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20181205_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Время'),
        ),
    ]