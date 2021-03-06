# Generated by Django 3.2 on 2021-07-20 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tst_app', '0015_alter_trip_classtrain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='Classtrain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tst_app.train'),
        ),
        migrations.AlterField(
            model_name='user',
            name='my_trips',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tst_app.trip'),
        ),
    ]
