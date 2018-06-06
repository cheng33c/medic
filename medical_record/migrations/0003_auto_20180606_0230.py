# Generated by Django 2.0.5 on 2018-06-06 02:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_record', '0002_auto_20180606_0229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='create_date',
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='create_datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 6, 2, 30, 49, 529314), verbose_name='病历创建时间'),
        ),
    ]
