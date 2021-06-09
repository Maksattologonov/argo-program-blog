from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Category, Course
from drf_multiple_model.views import ObjectMultipleModelAPIView


class CategoriesAndCourses(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



