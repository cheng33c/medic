# Generated by Django 2.0.5 on 2018-06-06 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical_record', '0006_auto_20180606_0236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalrecord',
            old_name='create_datetime',
            new_name='create_date',
        ),
    ]
