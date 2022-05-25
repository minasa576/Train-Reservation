# Generated by Django 3.2 on 2021-07-16 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(blank=True, choices=[('Luxurious, Wide,Single Seat', 'Luxurious, Wide,Single Seat')], max_length=50, null=True)),
                ('type', models.CharField(blank=True, choices=[('Direct , Non Stop', 'Direct , Non Stop')], max_length=50, null=True)),
                ('private_screens', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True)),
                ('free_snacks', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True)),
                ('USB_support', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True)),
                ('Earphone', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True)),
                ('WIFi', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True)),
                ('WC', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_no', models.IntegerField()),
                ('Departure_Time', models.TimeField(blank=True, null=True)),
                ('Arrival_Time', models.TimeField(blank=True, null=True)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tst_app.train')),
            ],
        ),
    ]
