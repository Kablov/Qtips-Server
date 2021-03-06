# Generated by Django 2.1 on 2018-11-21 13:01

import api.models.token
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_phone_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='phone',
        ),
        migrations.AddField(
            model_name='token',
            name='profile',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='api.Profile', verbose_name='Профиль'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(default=api.models.token.Token.get_new_token, max_length=32, unique=True, validators=[django.core.validators.MinLengthValidator(32)], verbose_name='Токен'),
        ),
    ]
