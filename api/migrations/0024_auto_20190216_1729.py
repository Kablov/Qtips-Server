# Generated by Django 2.1.2 on 2019-02-16 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20190214_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawrequest',
            name='reviewed_time',
            field=models.DateTimeField(blank=True, verbose_name='Время рассмотрения'),
        ),
    ]
