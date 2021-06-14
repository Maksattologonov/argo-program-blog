from django.db import models
from rest_framework import status
from rest_framework.response import Response
from django.db.models.functions import Coalesce


# Serializer mixins
class CoursesMixin:
    serializer = None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['courses'] = self.serializer(
            instance.courses.all().annotate(
                middle_star=Coalesce(models.Sum('rating__star')/models.Count('rating'), 5.0), many=True
            )
        ).data
        return representation


class TopicsAndRatingMixin:
    '''Course's topics, ratings and comments'''
    serializer1 = None
    serializer2 = None
    serializer3 = None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['topics'] = self.serializer1(instance.topics.all(),
                                                    many=True).data
        representation['rating'] = self.serializer2(instance.rating.all(),
                                                    many=True).data
        representation['commnets'] = self.serializer3(instance.comments.all(),
                                                      many=True).data
        return representation


class LessonsMixin:
    serializer = None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['lessons'] = self.serializer(instance.lessons.all(),
                                                    many=True).data
        return representation


class ContactsMediasMixin:
    serializer1 = None
    serializer2 = None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['contacts'] = self.serializer1(instance.contacts.all(),
                                                      many=True).data
        representation['medias'] = self.serializer2(instance.medias.all(),
                                                    many=True).data
        return representation


# Views mixins
class CreateMixin:
    serializer_class = None
    model = None

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if self.model.objects.filter(user=request.data['user'],
                                     course=request.data['course']):
            return Response('cannot evaluete again')
        else:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED,
                            headers=headers)
