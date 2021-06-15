from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Course
from ..serializers import CourseSerializer


class CourseApiTestCase(APITestCase):
    def test_create_course(self):
        course_1 = Course.objects.create(title='test title name1', description='test text', price=100,
                                         category='category_id')
        course_2 = Course.objects.create(title='test title name2', description='test text2', price=100,
                                         category='category_id')
        url = reverse('course_list')
        response = self.client_get(url)
        serializer_data = CourseSerializer([course_1, course_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
