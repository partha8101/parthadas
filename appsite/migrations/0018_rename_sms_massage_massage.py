# Generated by Django 3.2.6 on 2021-10-09 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0017_massage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='massage',
            old_name='sms',
            new_name='massage',
        ),
    ]
