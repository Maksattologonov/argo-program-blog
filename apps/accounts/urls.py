from django.conf.urls import url
from django.urls import path, include
from knox import views as knox_views
from .views import (
    RegistrationAPI, LoginAPI, UserAPI)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Program Blog",
        default_version='v1',
        description="Url for program blog site",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('register/', RegistrationAPI.as_view()),
    path('', include('knox.urls')),
    path('user/', UserAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    url(r'^swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
