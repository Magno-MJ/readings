import pytest

from src.application.use_cases.create_book_use_case import (
    CreateBookDto,
    CreateBookUseCase,
    BookAlreadyRegisteredException
)

from src.domain.entities.book import Book


@pytest.fixture
def book_repository(mocker):

    return mocker.Mock()


class TestCreateBookUseCase:

    def test_should_create_book_successfully(
        self,
        book_repository
    ):

        book_repository.find_by_isbn.return_value = None

        use_case = CreateBookUseCase(
            book_repository=book_repository
        )

        dto = CreateBookDto(
            name="Fake",
            quantity_of_pages=200,
            isbn="123456"
        )

        use_case.execute(dto)

        book_repository.find_by_isbn.assert_called_once_with(
            isbn=dto.isbn
        )

        book_repository.save.assert_called_once()

        saved_book = (
            book_repository.save.call_args.args[0]
        )

        assert saved_book.name == dto.name

        assert (
            saved_book.quantity_of_pages
            == dto.quantity_of_pages
        )

        assert saved_book.isbn == dto.isbn

    def test_should_raise_exception_when_book_already_exists(
        self,
        book_repository
    ):

        book_repository.find_by_isbn.return_value = Book(
            name="Existing Book",
            quantity_of_pages=100,
            isbn="123456"
        )

        use_case = CreateBookUseCase(
            book_repository=book_repository
        )

        dto = CreateBookDto(
            name="Fake",
            quantity_of_pages=200,
            isbn="123456"
        )

        with pytest.raises(
            BookAlreadyRegisteredException
        ):

            use_case.execute(dto)

        book_repository.find_by_isbn.assert_called_once_with(
            isbn=dto.isbn
        )

        book_repository.save.assert_not_called()
