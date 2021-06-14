from django.db import models
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (CategorySerializer, CommentSerializer,
                          CourseSerializer, CompanySerializer,
                          CategoryListSerializer, CoursesSerializer, RatingSerializer,
                          FavoriteSerializer, CommentCreateSerializer)
from .models import Category, Comment, Course, Company, Favorite, Rating
from .servises import CreateMixin
from .permissinos import IsOwner
from .pagination import CoursePagination
from .filters import CoursePriceFilter


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
            user=request.user
        ).exists()
        return Response(data={
            'data': serializer.data,
            'is_favorite': is_favorite
        })


class Categories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class AllCourses(generics.ListAPIView):
    '''Api for page with all categories and courses'''
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend, )
    filterset_class = CoursePriceFilter
    


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
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteDelete(generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (IsOwner,)


class FavoritesList(generics.ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        favorites = Favorite.objects.filter(user=self.request.user) 
        return favorites
