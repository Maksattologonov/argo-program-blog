from django.db.models import manager
from rest_framework import serializers
from .models import Course, Category, CourseTopic, Rating, TopicLesson, Company, Contact, SocialMedia
from .servises import CoursesMixin, LessonsMixin, TopicsAndRatingMixin, ContactsMediasMixin


class CoursesSerializer(serializers.ModelSerializer):
    """Courses list"""

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'price', 'category')


class CategorySerializer(CoursesMixin, serializers.ModelSerializer):
    """Categories List"""
    serializer = CoursesSerializer

    class Meta:
        model = Category
        fields = ('id', 'title')


class LessonSerializer(serializers.ModelSerializer):
    """Lesson details"""

    class Meta:
        model = TopicLesson
        fields = ('id', 'title', 'serial_number', 'topic')


class TopicSerializer(LessonsMixin, serializers.ModelSerializer):
    """Topic List"""
    serializer = LessonSerializer

    class Meta:
        model = CourseTopic
        fields = ('id', 'title', 'serial_number', 'course')

class RatingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'star', 'course', 'user')


class CourseSerializer(TopicsAndRatingMixin, serializers.ModelSerializer):
    """Course details"""
    serializer = TopicSerializer
    serializer2 = RatingCreateSerializer

    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    middle_star = serializers.FloatField(read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'price',  'middle_star', 'category')


class ContactSerializer(serializers.ModelSerializer):
    """Contact details"""

    class Meta:
        model = Contact
        fields = ('id', 'phone_number')


class MediaSerializer(serializers.ModelSerializer):
    """Media details"""

    class Meta:
        model = SocialMedia
        fields = ('id', 'media_name', 'url')


class CompanySerializer(ContactsMediasMixin, serializers.ModelSerializer):
    """Lesson details"""
    serializer1 = ContactSerializer
    serializer2 = MediaSerializer

    class Meta:
        model = Company
        fields = ('id', 'title', 'description')
