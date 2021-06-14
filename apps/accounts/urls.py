from django.conf.urls import url
from django.urls import path, include
from knox import views as knox_views
from .views import (
    RegistrationAPI, LoginAPI, UserAPI)
urlpatterns = [
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('user/', UserAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]
