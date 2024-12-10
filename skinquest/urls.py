# urls.py
from django.urls import path, include
from rest_framework import routers

from .views import (
    UserProfileViewSet,
    UserRegisterViewSet
)

router = routers.DefaultRouter()
router.register(r'profile', UserProfileViewSet, basename='user-profile')
router.register(r'register', UserRegisterViewSet, basename='user-register')

urlpatterns = [
    path('', include(router.urls)),
]

