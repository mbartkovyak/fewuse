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
from django.views.decorators.csrf import csrf_exempt

from fewuse.views import google_auth_callback, google_auth_redirect
from lendloop.viewsets import ProductViewSet, CategoryViewSet, OrderViewSet, ReviewViewSet
from rest_framework.authtoken.views import obtain_auth_token
from lendloop.views import registration_view
from telegram.views import accept_telegram_message
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from graphene_django.views import GraphQLView
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView


router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('orders', OrderViewSet)
router.register('reviews', ReviewViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/auth/", obtain_auth_token),
    path('api/', include(router.urls)),
    path('api/register/', registration_view),
    path('telegram/', accept_telegram_message),
    path('api/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path("", TemplateView.as_view(template_name="index.html")),
    path("accounts/", include("allauth.urls")),
    path("logout", LogoutView.as_view()),

]


