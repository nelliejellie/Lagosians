# Generated by Django 3.0.2 on 2020-05-28 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_image_total_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
