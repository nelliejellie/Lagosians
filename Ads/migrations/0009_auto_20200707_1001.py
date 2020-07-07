# Generated by Django 3.0.2 on 2020-07-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0008_auto_20200705_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='suscriptions',
            field=models.CharField(blank=True, choices=[('weekly', 'weekly'), ('monthly', 'monthly'), ('yearly', 'yearly')], max_length=20),
        ),
    ]