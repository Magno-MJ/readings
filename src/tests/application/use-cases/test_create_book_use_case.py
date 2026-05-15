import pytest

from unittest.mock import Mock

from src.application.use_cases.create_book_use_case import (
    CreateBookDto,
    CreateBookUseCase,
    BookAlreadyRegisteredException
)

from src.domain.entities.book import Book


class TestCreateBookUseCase:

    def test_should_create_book_successfully(self):

        repository = Mock()

        repository.find_by_isbn.return_value = None

        use_case = CreateBookUseCase(
            book_repository=repository
        )

        dto = CreateBookDto(
            name="DDD",
            quantity_of_pages=200,
            isbn="123456"
        )

        use_case.execute(dto)

        repository.find_by_isbn.assert_called_once_with(
            isbn=dto.isbn
        )

        repository.save.assert_called_once()

        saved_book = (
            repository.save.call_args.args[0]
        )

        assert saved_book.name == dto.name

        assert (
            saved_book.quantity_of_pages
            == dto.quantity_of_pages
        )

        assert saved_book.isbn == dto.isbn

    def test_should_raise_exception_when_book_already_exists(self):

        repository = Mock()

        repository.find_by_isbn.return_value = Book(
            name="Existing Book",
            quantity_of_pages=100,
            isbn="123456"
        )

        use_case = CreateBookUseCase(
            book_repository=repository
        )

        dto = CreateBookDto(
            name="DDD",
            quantity_of_pages=200,
            isbn="123456"
        )

        with pytest.raises(
            BookAlreadyRegisteredException
        ):

            use_case.execute(dto)

        repository.find_by_isbn.assert_called_once_with(
            isbn=dto.isbn
        )

        repository.save.assert_not_called()
