# Generated by Django 2.0.5 on 2018-06-06 02:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_record', '0003_auto_20180606_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='create_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='病历创建时间'),
        ),
    ]
