"""
URL configuration for skincare_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from skinquest.views import UserRegisterViewSet, UserProfileViewSet
from django.contrib.auth.views import LoginView

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'register', UserRegisterViewSet, basename='user-register')
router.register(r'profile', UserProfileViewSet, basename='user-profile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API endpoints for registration and profile management
    path('login/', LoginView.as_view(), name='login'),  # URL for login
    
]
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from skinquest.views import UserRegisterViewSet, UserProfileViewSet
from django.contrib.auth.views import LoginView, LogoutView

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'register', UserRegisterViewSet, basename='user-register')
router.register(r'profile', UserProfileViewSet, basename='user-profile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('skinquest.urls'), name='home'),
    path('api/', include(router.urls)),  # API endpoints for registration and profile management
    path('login/', LoginView.as_view(), name='login'),  # URL for login
    path('logout/', LogoutView.as_view(), name='logout'),  # URL for logout
]