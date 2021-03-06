from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CoursePagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'p'


    def get_paginated_response(self, data):
        return Response({
            'pages_count': self.page.paginator.num_pages,
            'results': data
        })
