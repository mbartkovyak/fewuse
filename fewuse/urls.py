"""
URL configuration for lendloop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from lendloop.viewsets import ProductViewSet, CategoryViewSet, AvailabilityViewSet
from rest_framework.authtoken.views import obtain_auth_token
from lendloop.views import registration_view

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('availabilities', AvailabilityViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", obtain_auth_token),
    path('api/', include(router.urls)),
    path('api/register/', registration_view),
]


