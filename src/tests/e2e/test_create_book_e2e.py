import pytest

from rest_framework.test import APIClient

from src.infra.database.models.book import (
    DjangoBook
)


@pytest.mark.django_db
class TestCreateBookE2E:

    def test_should_create_book_successfully(self):

        client = APIClient()

        payload = {
            "name": "Fake",
            "quantity_of_pages": 560,
            "isbn": "9788576082675"
        }

        response = client.post(
            "/api/books/",
            data=payload,
            format="json"
        )

        assert response.status_code == 201

        registered_book = (
            DjangoBook.objects.filter(
                isbn=payload["isbn"]
            ).first()
        )

        assert registered_book is not None

        registered_book_name = registered_book.name
        response_payload_name = payload.get("name")

        assert (registered_book_name == response_payload_name)

        registered_quantity_of_pages = registered_book.quantity_of_pages
        response_quantity_of_pages = payload.get("quantity_of_pages")

        assert (
            registered_quantity_of_pages == response_quantity_of_pages
        )

        registered_isbn = registered_book.isbn
        response_isbn = payload.get("isbn")

        assert (registered_isbn == response_isbn)
