# Generated by Django 4.2.5 on 2024-06-22 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_image_url_user_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image_url',
        ),
    ]