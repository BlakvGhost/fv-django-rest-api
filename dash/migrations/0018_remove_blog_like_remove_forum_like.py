# Generated by Django 4.0.3 on 2022-04-22 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0017_remove_like_value_like_is_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='like',
        ),
        migrations.RemoveField(
            model_name='forum',
            name='like',
        ),
    ]
