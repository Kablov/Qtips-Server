# Generated by Django 2.1.2 on 2019-03-16 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20190309_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cp_transaction_id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sa_transaction_id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='cp_transaction_id',
            field=models.CharField(blank=True, max_length=50, verbose_name='id транзакции в cloudpayments'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sa_transaction_id',
            field=models.CharField(blank=True, max_length=50, verbose_name='id транзакции в нашем банке'),
        ),
    ]
