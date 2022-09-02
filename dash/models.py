from django.db import models
from django.contrib.auth.models import User


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', null=True, on_delete=models.SET_NULL)
    post_id = models.IntegerField(null=True, blank=False)
    post_type = models.CharField(max_length=255, null=True, blank=False)
    is_liked = models.BooleanField(null=True, blank=False)
    is_like = models.BooleanField(null=True, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.user.username


class View(models.Model):
    post_id = models.IntegerField(null=True, blank=False)
    post_type = models.CharField(max_length=255, null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    ipaddress = models.GenericIPAddressField(null=True, blank=False)
    user_a = models.CharField(max_length=255, null=True, blank=False)

    def __str__(self):
        return f"{self.ipaddress}"


class Category(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    icon = models.CharField(max_length=255, null=True, blank=False)
    description = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post_id = models.IntegerField(null=True, blank=False)
    post_type = models.CharField(max_length=255, null=True, blank=False)
    content = models.TextField(null=True, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.content


class Blog(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255, null=True, blank=False)
    cover = models.ImageField(upload_to='blog', null=True)
    content = models.TextField(null=True, blank=False)
    category = models.ForeignKey(Category, related_name="blogs", null=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_created=True, null=False)
    update_date = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.title


class Forum(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.TextField(null=True, blank=False)
    category = models.ForeignKey(Category, related_name="forums", null=True, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, null=False)
    update_date = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    cover = models.ImageField(upload_to='gallery', null=True)
    title = models.CharField(max_length=255, null=True, blank=False)

    def __str__(self):
        return self.title


class Post(models.Model):
    user_id = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    sup_title = models.CharField(max_length=255, null=True, blank=False)
    sub_title = models.CharField(max_length=255, null=True, blank=False)
    content = models.TextField(null=True, blank=False)
    visible = models.BooleanField(null=True, blank=False)
    carousel = models.BooleanField(null=True, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True, null=False)
    cover = models.ImageField(upload_to='post', null=True)

    def __str__(self):
        return self.sup_title


class PublicMail(models.Model):
    user_id = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=255, null=True, blank=False)
    last_name = models.CharField(max_length=255, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    message = models.TextField(null=True, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.email


class About(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False)
    experience = models.CharField(max_length=255, null=True, blank=False)
    support = models.CharField(max_length=255, null=True, blank=False)
    content = models.TextField(null=True, blank=False)
    visible = models.BooleanField(null=True, blank=False)
    gallery = models.ManyToManyField(Gallery)

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    icon = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=False)
    logo = models.ImageField(upload_to='partner', null=True, blank=True)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    icon = models.CharField(max_length=255, null=True, blank=False)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    link = models.URLField(max_length=255, null=True, blank=False)
    cat = models.CharField(max_length=255, null=True, blank=False)
    cover = models.ImageField(upload_to='project', null=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    title = models.CharField(max_length=255, null=True, blank=False)
    icon = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True, blank=False)
    logo = models.ImageField(upload_to='client', null=True, blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    nom = models.CharField(max_length=255, null=True, blank=False)
    prenom = models.CharField(max_length=255, null=True, blank=False)
    role = models.CharField(max_length=255, null=True, blank=False)
    desc = models.TextField(null=True, blank=False)
    photo = models.ImageField(upload_to='client', null=True, blank=False)

    def __str__(self):
        return self.nom


class Partner(models.Model):
    icon = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=False)
    logo = models.ImageField(upload_to='partner', null=True, blank=True)

    def __str__(self):
        return self.name


class Util(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    value = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.name


class WhyShooseUs(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    icon = models.CharField(max_length=255, null=True, blank=False)
    content = models.TextField(null=True, blank=False)
    value = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return self.name
