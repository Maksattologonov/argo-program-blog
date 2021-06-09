
from django.db import models

class CoursesMixin:
    serializer1 = None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['courses'] = self.serializer1(instance.courses.all(), many=True).data
        return representation


class TopicsAndRatingMixin:
    serializer = None
    serializer2 = None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['topics'] = self.serializer(instance.topics.all(), many=True).data
        representation['rating'] = self.serializer2(instance.rating.all(), many=True).data
        return representation


class LessonsMixin:
    serializer = None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['lessons'] = self.serializer(instance.lessons.all(), many=True).data
        return representation

class ContactsMediasMixin:
    serializer1 = None
    serializer2 = None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['contacts'] = self.serializer1(instance.contacts.all(), many=True).data
        representation['medias'] = self.serializer2(instance.medias.all(), many=True).data
        return representation
