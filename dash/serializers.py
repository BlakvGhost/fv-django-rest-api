from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . import models


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'password2', 'email', 'first_name', 'last_name']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                "password": "Les Deux Mots de Passe ne sont Pas identiques."
            })
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        g = Group.objects.get(name="FuturaVision Members")
        g.user_set.add(user)
        return user


class LikesSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False, default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Like
        fields = ['id', 'post_id', 'post_type', 'user', 'pub_date', 'is_liked', 'is_like']


class ViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.View
        fields = '__all__'
        read_only_fields = ['ipaddress', 'user_a']

    def create(self, validated_data):
        ip = self.context['request'].META['REMOTE_ADDR']
        ua = self.context['request'].META['HTTP_USER_AGENT']
        like = models.View.objects.filter(
            ipaddress=ip,
            post_type=validated_data['post_type'],
            post_id=validated_data['post_id'])

        if like.count() == 0:
            return models.View.objects.create(
                post_type=validated_data['post_type'],
                post_id=validated_data['post_id'],
                ipaddress=ip,
                user_a=ua
            )
        return like[0]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Post
        fields = ['id', 'sup_title', 'sub_title', 'content', 'carousel', 'visible', 'cover', 'pub_date', ]


class PublicMailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PublicMail
        fields = ['id', 'first_name', 'last_name', 'email', 'message', 'pub_date', ]


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Gallery
        fields = ['id', 'title', 'cover']


class AboutSerializer(serializers.HyperlinkedModelSerializer):
    gallery = GallerySerializer(many=True)

    class Meta:
        model = models.About
        fields = ['experience', 'support', 'title', 'content', 'visible', 'gallery']


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Service
        fields = ['id', 'icon', 'name', 'content', 'logo']


class TechnologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Technology
        fields = ['id', 'icon', 'name', 'content', ]


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Team
        fields = ['id', 'nom', 'prenom', 'role', 'desc', 'photo']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Project
        fields = ['id', 'name', 'link', 'cat', 'cover']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Client
        fields = ['id', 'name', 'title', 'content', 'logo']


class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Partner
        fields = ['id', 'name', 'logo', 'icon']


class UtilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Util
        fields = ['name', 'value']


class WhyShooseUsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.WhyShooseUs
        fields = ['id', 'name', 'content', 'value', 'icon']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False, default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Comment
        fields = ['id', 'user', 'content', 'pub_date', 'post_id', 'post_type']


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False)
    category = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')

    class Meta:
        model = models.Blog
        fields = [
            'id', 'title', 'content', 'cover', 'category',
            'pub_date', 'update_date', 'user',
        ]


class ForumSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(many=False, read_only=False, slug_field='name', queryset=models.Category.objects.all())
    user = UserSerializer(many=False, default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Forum
        fields = [
            'id', 'title', 'user', 'category',
            'pub_date', 'update_date'
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    blogs = BlogSerializer(many=True)
    forums = ForumSerializer(many=True)

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'description', 'icon', 'blogs', 'forums']
