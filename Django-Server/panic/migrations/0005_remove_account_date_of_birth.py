# Generated by Django 2.1.2 on 2018-10-18 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panic', '0004_auto_20181018_0432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='date_of_birth',
        ),
    ]
