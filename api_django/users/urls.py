from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'user_profile', views.UserProfileView, basename='user-profile')
router.register(r'user_list', views.UsersListView, basename='user-list')
router.register(r'user_registration', views.UserRegistration, basename='user-registration')

urlpatterns = [
    path('', include(router.urls)),
]


