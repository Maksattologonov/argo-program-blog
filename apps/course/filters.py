from django_filters import rest_framework
from .models import Course


class CourseFilter(rest_framework.FilterSet):
    price = rest_framework.RangeFilter()

    class Meta:
        model = Course
        fields = ['price', 'category',]

class CoursePriceFilter(rest_framework.FilterSet):
    price = rest_framework.RangeFilter()

    class Meta:
        model = Course
        fields = ['price',]