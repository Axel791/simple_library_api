from django.urls import path, include, re_path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', views.UsersView, basename='user-methods')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]
