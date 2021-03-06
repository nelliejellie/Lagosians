# Generated by Django 3.0.2 on 2020-08-27 18:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0008_auto_20200827_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='count_likes',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='like',
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.ManyToManyField(related_name='comment_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
