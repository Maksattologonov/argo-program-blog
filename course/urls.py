from django.urls import path
from .views import CategoriesAndCourses, CourseDetails, CompanyDetails

urlpatterns = [
    path('', CategoriesAndCourses.as_view(), name='categories'),
    path('<str:pk>/', CourseDetails.as_view(), name='course_details'),
    path('about_us/', CompanyDetails.as_view(), name='about_us'),


]