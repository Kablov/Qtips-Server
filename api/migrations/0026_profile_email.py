# Generated by Django 2.1.2 on 2019-02-16 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20190216_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email'),
        ),
    ]
