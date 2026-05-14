from django.urls import path

from src.infra.http.views.create_book_api_view import (
    CreateBookAPIView
)

urlpatterns = [
    path(
        "",
        CreateBookAPIView.as_view()
    ),
]
