# Generated by Django 4.0.6 on 2022-08-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_post_likes_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.BigIntegerField(default=0),
        ),
    ]
