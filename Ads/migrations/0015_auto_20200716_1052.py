# Generated by Django 3.0.2 on 2020-07-16 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0014_auto_20200716_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='created',
            field=models.DateField(db_index=True, default=datetime.datetime.now),
        ),
    ]