# Generated by Django 2.1.2 on 2018-11-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20181128_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='payment_url',
            field=models.CharField(blank=True, max_length=45, verbose_name='URL страницы оплаты'),
        ),
    ]
