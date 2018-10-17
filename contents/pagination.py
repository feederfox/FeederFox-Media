from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from .models import Article
from django.http import HttpResponse
from rest_framework.response import Response


class PostLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 4
	max_limit = 10

class PostPageNumberPagination(PageNumberPagination):
	page_size = 1


class ArticlePagination():
	a = Article.objects.all()
	print(a)
	pass


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })	