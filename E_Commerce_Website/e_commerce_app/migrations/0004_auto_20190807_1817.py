# Generated by Django 2.2.3 on 2019-08-07 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0003_signup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='password1',
            new_name='confirm_password',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='password2',
            new_name='password',
        ),
    ]