from django.db import models
from rest_framework import generics
from rest_framework.views import APIView
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import (CategorySerializer, CommentSerializer,
                          CourseSerializer, CompanySerializer,
                          CategoryListSerializer, CoursesSerializer, RatingSerializer,
                          FavoriteSerializer)
from .models import Category, Comment, Course, Company, Favorite, Rating
from .servises import CreateMixin
from .permissinos import IsOwner
from .pagination import CoursePagination


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
        course = Course.objects.filter(id=kwargs.get('pk'))
        course = course.annotate(middle_star=models.Sum(
            'rating__star'
        )/models.Count('rating'))
        serializer = CourseSerializer(course[0], many=False)
        is_favorite = Favorite.objects.filter(
            course=kwargs.get('pk'),
            user=request.user #TODO: CHANGE ON REQUEST USER
        ).exists()
        return Response(data={
            'data': serializer.data,
            'is_favorite': is_favorite
        })


class AllCourses(ObjectMultipleModelAPIView):
    '''Api for page with all categories and courses'''
    querylist = [
        {'queryset': Category.objects.all(),
         'serializer_class': CategoryListSerializer},
        {'queryset': Course.objects.all(),
         'serializer_class': CoursesSerializer,},
    ]
    


class CategoryCourses(generics.ListAPIView):
    '''Api for one category with its courses'''
    serializer_class = CoursesSerializer
    pagination_class = CoursePagination

    def get_queryset(self):
        courses = Course.objects.filter(category=self.kwargs['pk'])
        return courses


class RatingCreate(CreateMixin, generics.CreateAPIView):
    '''
    Api for create rating.
    Have a mixin thet cheking if rating for course from user exists
    '''
    serializer_class = RatingSerializer
    model = Rating
    permission_classes = (IsAuthenticated,)


class CommentCreate(generics.CreateAPIView):
    '''Api for create comment'''
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)


class CommentUpdate(generics.UpdateAPIView):
    '''Api for update comment'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = IsOwner
    http_method_names = ('patch',)


class CommentDelete(generics.DestroyAPIView):
    '''Api for delete comment'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwner,)


class FavoriteAdd(generics.CreateAPIView):
    serializer_class = FavoriteSerializer
    model = Favorite
    permission_classes = (IsAuthenticated,)


class FavoriteDelete(generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (IsOwner,)


class FavoritesList(generics.ListAPIView):
    queryset = Favorite.objects.filter(user=1) #TODO: CHANGE ON REQUEST USER
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticated,)
