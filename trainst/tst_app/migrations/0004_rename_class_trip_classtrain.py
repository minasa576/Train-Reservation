# Generated by Django 3.2 on 2021-07-17 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tst_app', '0003_alter_trip_seats'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='Class',
            new_name='Classtrain',
        ),
    ]
