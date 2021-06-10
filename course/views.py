from django.db import models
from rest_framework import generics
from rest_framework.views import APIView
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.response import Response
from .serializers import (CategorySerializer, CommentSerializer, CourseSerializer,
                          CompanySerializer, CategoryListSerializer,
                          RatingSerializer)
from .models import Category, Comment, Course, Company, Rating
from .servises import RatingCreateMixin



class CompanyDetails(APIView):
    '''Api for page about company'''
    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response({'company': serializer.data})



class CategoriesWithCourses(generics.ListAPIView):
    '''Api for home page where only 4 courses for every category'''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CourseDetails(APIView):
    '''Api for all details for course with lessons, ratings and comments'''
    def get(self, request, *args, **kwargs):
        course = Course.objects.filter(
            id=kwargs.get('pk')
        ).annotate(middle_star=models.Sum(
            'rating__star'
        )/models.Count('rating'))
        serializer = CourseSerializer(course[0], many=False)
        return Response(data={
            'data': serializer.data
        })


class AllCourses(ObjectMultipleModelAPIView):
    '''Api for page with all categories and courses'''
    querylist = [
        {'queryset': Category.objects.all(),
         'serializer_class': CategoryListSerializer},
        {'queryset': Course.objects.all(),
         'serializer_class': CourseSerializer},
    ]


class CategoryCourses(generics.RetrieveAPIView):
    '''Api for one category with its courses'''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RatingCreate(RatingCreateMixin, generics.CreateAPIView):
    '''
    Api for create rating.
    Have a mixin thet cheking if rating for course from user exists
    '''
    serializer_class = RatingSerializer


class CommentCreate(generics.CreateAPIView):
    '''Api for create comment'''
    serializer_class = CommentSerializer


class CommentUpdate(generics.UpdateAPIView):
    '''Api for update comment'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['patch',]


class CommentDelete(generics.DestroyAPIView):
    '''Api for delete comment'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
