from rest_framework import pagination
from rest_framework.response import Response


class NumberedPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        next_page = None
        prev_page = None

        if self.page.has_next():
            next_page = self.page.next_page_number()

        if self.page.has_previous():
            prev_page = self.page.previous_page_number()

        return Response({
            'next': next_page,
            'previous': prev_page,
            'count': self.page.paginator.count,
            'results': data
        })