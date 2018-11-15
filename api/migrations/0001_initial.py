# Generated by Django 2.1.2 on 2018-11-15 20:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Код страны')),
                ('number', models.CharField(max_length=14, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Номер телефона',
                'verbose_name_plural': 'Номера телефонов',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_id', models.IntegerField(unique=True, validators=[django.core.validators.RegexValidator('^\\d{6}$')])),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('photo', models.TextField(blank=True, null=True, verbose_name='Ссылка на фото')),
                ('status', models.CharField(choices=[('pure', 'Чистый'), ('banned', 'Забанен')], default='pure', max_length=7, verbose_name='Статус')),
                ('phone', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Phone', verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]