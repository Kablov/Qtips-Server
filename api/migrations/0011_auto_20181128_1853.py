# Generated by Django 2.1.2 on 2018-11-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_smscode_udid'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Баланс'),
        ),
        migrations.AddField(
            model_name='profile',
            name='payment_url',
            field=models.CharField(blank=True, max_length=50, verbose_name='URL страницы оплаты'),
        ),
        migrations.AddField(
            model_name='profile',
            name='qr',
            field=models.TextField(blank=True, null=True, verbose_name='QR-код'),
        ),
    ]
