# Generated by Django 2.2.4 on 2023-06-16 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvapp', '0004_auto_20230616_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='release_date',
        ),
    ]
