from dataclasses import dataclass

from src.domain.repositories.book_repository import BookRepository
from src.domain.entities.book import Book


@dataclass
class CreateBookDto:
    name: str
    quantity_of_pages: int
    isbn: str


class BookAlreadyRegisteredException(Exception):
    def __init__(self):
        self.message = "Book already exists"
        super().__init__(self.message)


class CreateBookUseCase:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, dto: CreateBookDto):
        isbn = dto.isbn
        registered_book = self.book_repository.find_by_isbn(isbn=isbn)

        if registered_book:
            raise BookAlreadyRegisteredException()

        book = Book(
            name=dto.name,
            quantity_of_pages=dto.quantity_of_pages,
            isbn=dto.isbn
        )

        self.book_repository.save(book)
