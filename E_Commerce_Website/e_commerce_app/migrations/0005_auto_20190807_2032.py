# Generated by Django 2.2.3 on 2019-08-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0004_auto_20190807_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='confirm_password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
