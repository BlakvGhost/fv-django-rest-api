# Generated by Django 4.0.3 on 2022-04-21 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0007_blog_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='comment',
        ),
    ]