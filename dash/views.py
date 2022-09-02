from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework import viewsets
from . import models
from . import serializers

# @csrf_exempt
from .paginations import StandardResultsSetPagination, CommentResultsSetPagination


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all().order_by('-id')
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = models.Service.objects.all().order_by('-id')
    serializer_class = serializers.ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PublicMailViewSet(viewsets.ModelViewSet):
    queryset = models.PublicMail.objects.all().order_by('-id')
    serializer_class = serializers.PublicMailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AboutViewSet(viewsets.ModelViewSet):
    queryset = models.About.objects.all().order_by('-id')
    serializer_class = serializers.AboutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = models.Gallery.objects.all().order_by('-id')
    serializer_class = serializers.GallerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = models.Partner.objects.all().order_by('-id')
    serializer_class = serializers.PartnerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all().order_by('-id')
    serializer_class = serializers.ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WhyUsViewSet(viewsets.ModelViewSet):
    queryset = models.WhyShooseUs.objects.all().order_by('-id')
    serializer_class = serializers.WhyShooseUsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all().order_by('-id')
    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UtilsViewSet(viewsets.ModelViewSet):
    queryset = models.Util.objects.all().order_by('-id')
    serializer_class = serializers.UtilSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TechViewSet(viewsets.ModelViewSet):
    queryset = models.Technology.objects.all().order_by('-id')
    serializer_class = serializers.TechnologySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all().order_by('-id')
    serializer_class = serializers.TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all().order_by('-id')
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filterset_fields = ['name', 'forums', 'blogs']


class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all().order_by('-id')
    serializer_class = serializers.BlogSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PopularBlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all().order_by('-id')[:2]
    serializer_class = serializers.BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ForumViewSet(viewsets.ModelViewSet):
    queryset = models.Forum.objects.all().order_by('-id')
    serializer_class = serializers.ForumSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all().order_by('-id')
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = CommentResultsSetPagination
    filterset_fields = ['post_id', 'post_type']


class LikeViewSet(viewsets.ModelViewSet):
    queryset = models.Like.objects.all().order_by('-id')
    serializer_class = serializers.LikesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['post_id', 'post_type', 'is_liked', 'user', 'is_like']


class ViewViewSet(viewsets.ModelViewSet):
    queryset = models.View.objects.all().order_by('-id')
    serializer_class = serializers.ViewSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['post_id', 'post_type']


class UserAuthViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
