# from .serializers import CourseSerializer, CategoriesSerializer
# from .models import Category, Course
# from rest_framework import generics
from rest_framework import serializers
from .models import Course, Category

class CoursesMixin:
    serializer = None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['courses'] = self.serializer(instance.courses.all(), many=True).data
        return representation
