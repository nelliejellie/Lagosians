# Generated by Django 3.0.2 on 2020-06-29 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0002_auto_20200629_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='created',
            field=models.DateField(db_index=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateField(db_index=True, default=datetime.datetime.now),
        ),
    ]
