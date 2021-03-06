# Generated by Django 2.0.5 on 2018-06-05 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180605_0258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='name',
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='', max_length=6, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='users',
            name='image',
            field=models.ImageField(blank=True, default='upload/image/default.png', null=True, upload_to='upload/image/%Y/%m', verbose_name='用户头像'),
        ),
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='手机号码'),
        ),
    ]
