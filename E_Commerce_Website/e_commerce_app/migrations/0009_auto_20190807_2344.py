# Generated by Django 2.2.3 on 2019-08-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0008_auto_20190807_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producthistory',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='producthistory',
            name='total_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producthistory',
            name='unit_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
