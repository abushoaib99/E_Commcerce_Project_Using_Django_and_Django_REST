# Generated by Django 2.2.4 on 2019-08-06 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('available_quantity', models.PositiveIntegerField(default=0)),
                ('seller_name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(default=0)),
                ('select_quantity', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(upload_to='img')),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('update_on', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerce_app.Category')),
            ],
        ),
    ]
