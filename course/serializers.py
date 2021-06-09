from rest_framework import serializers
from .models import Course, Category
from .servises import CoursesMixin


class CourseSerializer(serializers.ModelSerializer):
    """Course details"""

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'price', 'category')


class CategorySerializer(CoursesMixin, serializers.ModelSerializer):
    """Categories List"""
    serializer = CourseSerializer

    class Meta:
        model = Category
        fields = ('id', 'title')



