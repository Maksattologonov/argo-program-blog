from django.db.models import fields
from rest_framework import serializers
from .models import (Course, Category, CourseTopic, Rating,
                     TopicLesson, Company, Contact, SocialMedia,
                     Comment, Favorite)
from .servises import (CoursesMixin, LessonsMixin,
                       TopicsAndRatingMixin, ContactsMediasMixin)


class CoursesSerializer(serializers.ModelSerializer):
    """Courses list"""
    middle_star = serializers.FloatField(read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'middle_star', 'price', 'category')


class CategoryListSerializer(serializers.ModelSerializer):
    """Categories List"""

    class Meta:
        model = Category
        fields = ('id', 'title')


class MediaSerializer(serializers.ModelSerializer):
    """Media details"""

    class Meta:
        model = SocialMedia
        fields = ('id', 'media_name', 'url')


class ContactSerializer(serializers.ModelSerializer):
    """Contact details"""

    class Meta:
        model = Contact
        fields = ('id', 'phone_number')


class CommentSerializer(serializers.ModelSerializer):
    """Media details"""

    class Meta:
        model = Comment
        fields = ('id', 'message', 'course', 'user')


class LessonSerializer(serializers.ModelSerializer):
    """Lesson details"""

    class Meta:
        model = TopicLesson
        fields = ('id', 'title', 'serial_number', 'topic')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'star', 'course', 'user')


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'course', 'user')


# Serializers with reprezentations
class CategorySerializer(CoursesMixin, serializers.ModelSerializer):
    """Categories List"""
    serializer = CoursesSerializer

    class Meta:
        model = Category
        fields = ('id', 'title')


class TopicSerializer(LessonsMixin, serializers.ModelSerializer):
    """Topic List"""
    serializer = LessonSerializer

    class Meta:
        model = CourseTopic
        fields = ('id', 'title', 'serial_number', 'course')


class CourseSerializer(TopicsAndRatingMixin, serializers.ModelSerializer):
    """Course details"""
    serializer1 = TopicSerializer
    serializer2 = RatingSerializer
    serializer3 = CommentSerializer

    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    middle_star = serializers.FloatField(read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'price',
                  'middle_star', 'category')



class CompanySerializer(ContactsMediasMixin, serializers.ModelSerializer):
    """Lesson details"""
    serializer1 = ContactSerializer
    serializer2 = MediaSerializer

    class Meta:
        model = Company
        fields = ('id', 'title', 'description')

