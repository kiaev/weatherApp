# Generated by Django 4.0.3 on 2022-04-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='CityName',
            field=models.CharField(max_length=255, verbose_name='CityName'),
        ),
    ]