# Generated by Django 4.0.3 on 2022-04-19 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('icon', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='client')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(null=True, upload_to='gallery')),
                ('title', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='partner')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('link', models.URLField(max_length=255, null=True)),
                ('cat', models.CharField(max_length=255, null=True)),
                ('cover', models.ImageField(null=True, upload_to='project')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('icon', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='partner')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, null=True)),
                ('prenom', models.CharField(max_length=255, null=True)),
                ('role', models.CharField(max_length=255, null=True)),
                ('desc', models.TextField(null=True)),
                ('photo', models.ImageField(null=True, upload_to='client')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('icon', models.CharField(max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Util',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('value', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WhyShooseUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('icon', models.CharField(max_length=255, null=True)),
                ('content', models.TextField(null=True)),
                ('value', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sup_title', models.CharField(max_length=255, null=True)),
                ('sub_title', models.CharField(max_length=255, null=True)),
                ('content', models.TextField(null=True)),
                ('visible', models.BooleanField(null=True)),
                ('carousel', models.BooleanField(null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('cover', models.ImageField(null=True, upload_to='post')),
                ('user_id', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('experience', models.CharField(max_length=255, null=True)),
                ('support', models.CharField(max_length=255, null=True)),
                ('content', models.TextField(null=True)),
                ('visible', models.BooleanField(null=True)),
                ('gallery', models.ManyToManyField(to='dash.gallery')),
            ],
        ),
    ]
