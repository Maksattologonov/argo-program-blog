from inspect import CO_ASYNC_GENERATOR
from django.db.models import manager
from django.shortcuts import render
from django.db import models
from rest_framework import generics, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import CategorySerializer, CourseSerializer, CompanySerializer
from .models import Category, Course, Company


# class CompanyDetails(generics.ListAPIView):
    # queryset = Company.objects.all()
    # serializer_class = CompanySerializer


class CompanyDetails(APIView):
    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response({'company': serializer.data})


class CategoriesAndCourses(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    


class CourseDetails(APIView):

    def get(self, request, *args, **kwargs):
        course = Course.objects.filter(id = kwargs.get('pk')).annotate(middle_star = models.Sum('rating__star') / models.Count('rating'))
        print(course)
        serializer = CourseSerializer(course[0], many=False)
        return Response(data={
            'data': serializer.data   
        })





