# Generated by Django 4.0.3 on 2022-04-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CityName', models.CharField(max_length=255)),
                ('Date', models.CharField(max_length=255)),
                ('Temperature', models.CharField(max_length=255)),
                ('MaxTemperature', models.CharField(max_length=255)),
                ('MinTemperature', models.CharField(max_length=255)),
                ('Humidity', models.CharField(max_length=255)),
                ('Date_YEAR_BEFORE', models.CharField(max_length=255)),
                ('Temperature_YEAR_BEFORE', models.CharField(max_length=255)),
                ('MaxTemperature_YEAR_BEFORE', models.CharField(max_length=255)),
                ('MinTemperature_YEAR_BEFORE', models.CharField(max_length=255)),
                ('Humidity_YEAR_BEFORE', models.CharField(max_length=255)),
            ],
        ),
    ]