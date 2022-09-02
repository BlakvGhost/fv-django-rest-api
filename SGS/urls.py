"""SGS URL Configuration

"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from SGS import settings
from dash import views
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register('services', views.ServicesViewSet, basename='services')
router.register('about', views.AboutViewSet, basename='about')
router.register('galleries', views.GalleryViewSet, basename='gallery')
router.register('partners', views.PartnerViewSet, basename='partner')
router.register('clients', views.ClientViewSet, basename='clients')
router.register('whyus', views.WhyUsViewSet, basename='whyus')
router.register('utils', views.UtilsViewSet, basename='utils')
router.register('tech', views.TechViewSet, basename='technology')
router.register('projects', views.ProjectViewSet, basename='project')
router.register('team', views.TeamViewSet, basename='team')
router.register('messages', views.PublicMailViewSet, basename='messages')
router.register('blog', views.BlogViewSet, basename='blog')
router.register('popularBlog', views.PopularBlogViewSet, basename='blogPopular')
router.register('forum', views.ForumViewSet, basename='forum')
router.register('category', views.CategoryViewSet, basename='category')
router.register('comments', views.CommentViewSet, basename='comment')
router.register('likes', views.LikeViewSet, basename='like')
router.register('les-vues', views.ViewViewSet, basename='view')
router.register('groups', views.GroupViewSet, basename='groups')
router.register('users', views.UserViewSet, basename='users')
router.register('user-auth', views.UserAuthViewSet, basename='user')

urlpatterns = [
                  path('', include(router.urls)),
                  path('admin/', admin.site.urls),
                  path('api/', include(router.urls)),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_pair'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
