import pytest

from rest_framework import status
from rest_framework.test import APIRequestFactory

from src.application.use_cases.create_book_use_case import (
    BookAlreadyRegisteredException,
    CreateBookDto,
)

from src.infra.http.views.create_book_api_view import (
    CreateBookAPIView
)


@pytest.fixture
def api_client_factory():
    return APIRequestFactory()


@pytest.fixture
def payload():
    return {
        "name": "Fake",
        "quantity_of_pages": 300,
        "isbn": "1234567890"
    }


@pytest.fixture
def mocked_use_case(mocker):
    return mocker.patch(
        "src.infra.http.views.create_book_api_view.create_book_use_case"
    )


class TestCreateBookAPIView:

    def test_should_return_201_created_when_book_is_created_successfully(
        self,
        api_client_factory,
        payload,
        mocked_use_case
    ):

        request = api_client_factory.post(
            "/api/books/",
            payload,
            format="json"
        )

        response = CreateBookAPIView.as_view()(request)

        assert response.status_code == (
            status.HTTP_201_CREATED
        )

        mocked_use_case.execute.assert_called_once_with(
            CreateBookDto(
                name=payload.get("name"),
                quantity_of_pages=payload.get(
                    "quantity_of_pages"
                ),
                isbn=payload.get("isbn")
            )
        )

    def test_should_return_400_bad_request_when_serializer_is_invalid(
        self,
        api_client_factory,
        mocked_use_case
    ):

        invalid_payload = {
            "name": "",
            "quantity_of_pages": 0,
            "isbn": "invalid"
        }

        request = api_client_factory.post(
            "/api/books/",
            invalid_payload,
            format="json"
        )

        response = CreateBookAPIView.as_view()(request)

        assert response.status_code == (
            status.HTTP_400_BAD_REQUEST
        )

        assert "message" in response.data

        mocked_use_case.execute.assert_not_called()

    def test_should_return_400_bad_request_when_book_already_exists(
        self,
        api_client_factory,
        payload,
        mocked_use_case
    ):

        request = api_client_factory.post(
            "/api/books/",
            payload,
            format="json"
        )

        mocked_use_case.execute.side_effect = (
            BookAlreadyRegisteredException()
        )

        response = CreateBookAPIView.as_view()(request)

        assert response.status_code == (
            status.HTTP_400_BAD_REQUEST
        )

        assert response.data == {
            "message": "Book already exists"
        }

        mocked_use_case.execute.assert_called_once_with(
            CreateBookDto(
                name=payload.get("name"),
                quantity_of_pages=payload.get(
                    "quantity_of_pages"
                ),
                isbn=payload.get("isbn")
            )
        )
