from rest_framework import routers
from .api import PostViewSet
from .views import RegisterAPI, LoginAPI
from django.urls import path

from knox import views as knox_views


router = routers.DefaultRouter()

router.register('api/blog', PostViewSet, 'posts')

urlpatterns = router.urls


urlpatterns.append(path('api/register/', RegisterAPI.as_view(), name='register'))
urlpatterns.append(path('api/login/', LoginAPI.as_view(), name='login'))
urlpatterns.append(path('api/logout/', knox_views.LogoutView.as_view(), name='logout'))
urlpatterns.append(path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'))

