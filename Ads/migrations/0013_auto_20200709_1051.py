# Generated by Django 3.0.2 on 2020-07-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0012_auto_20200709_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='daily_ad',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ads',
            name='monthly_ad',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ads',
            name='weekly_ad',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ads',
            name='yearly_ad',
            field=models.BooleanField(default=False),
        ),
    ]