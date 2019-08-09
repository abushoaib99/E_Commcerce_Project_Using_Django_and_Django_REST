# Generated by Django 2.2.3 on 2019-08-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0011_auto_20190808_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(max_length=11)),
                ('account_type', models.CharField(choices=[('BUYER', 'BUYER'), ('SELLER', 'SELLER')], max_length=8)),
            ],
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
    ]