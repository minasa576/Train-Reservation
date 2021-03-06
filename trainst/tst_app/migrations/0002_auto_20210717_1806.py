# Generated by Django 3.2 on 2021-07-17 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tst_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='from_station',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='seats',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='trip',
            name='to_station',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_no',
            field=models.CharField(max_length=100),
        ),
    ]
