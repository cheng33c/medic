# Generated by Django 2.0.5 on 2018-06-06 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20180606_1103'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='doctors',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_doctor',
        ),
    ]
