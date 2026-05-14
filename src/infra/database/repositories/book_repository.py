from src.domain.entities.book import Book
from src.domain.repositories.book_repository import BookRepository
from src.infra.database.mappers.book_mapper import BookMapper
from src.infra.database.models.book import DjangoBook


class DjangoBookRepository(BookRepository):
    def find_by_isbn(self, isbn: str) -> Book | None:
        try:
            book = DjangoBook.objects.get(isbn=isbn)

            return BookMapper.to_entity(book)
        except DjangoBook.DoesNotExist:
            return None

    def save(self, book: Book):
        DjangoBook.objects.create(
            name=book.name,
            quantity_of_pages=book.quantity_of_pages,
            isbn=book.isbn
        )
