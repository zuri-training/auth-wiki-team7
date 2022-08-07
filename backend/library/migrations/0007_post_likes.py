# Generated by Django 4.0.6 on 2022-07-30 09:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0006_post_adminupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='library_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
