from django.urls import path
from .views import CategoriesAndCourses

urlpatterns = [
    path('', CategoriesAndCourses.as_view(), name='categories'),

]