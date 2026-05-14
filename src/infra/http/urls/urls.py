from django.urls import include, path


urlpatterns = [
    path(
        "books/",
        include("src.infra.http.urls.book_urls")
    ),
]
