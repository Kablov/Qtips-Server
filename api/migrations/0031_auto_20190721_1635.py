# Generated by Django 2.2.3 on 2019-07-21 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20190721_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smscode',
            name='phone',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sms_code', to='api.Phone', verbose_name='Номер телефона'),
        ),
    ]
