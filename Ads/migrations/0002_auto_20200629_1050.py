# Generated by Django 3.0.2 on 2020-06-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='created',
            field=models.DateField(auto_now=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateField(auto_now=True, db_index=True),
        ),
    ]
