# Generated by Django 4.0.3 on 2022-04-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0009_alter_blog_user_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
