# Generated by Django 2.1.2 on 2018-12-04 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20181201_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='sum',
            new_name='amount',
        ),
    ]
