
from src.domain.entities.book import Book
from src.infra.database.models.book import DjangoBook


class BookMapper:
    def to_entity(book: DjangoBook):
        return Book(
            id=book.id,
            name=book.name,
            quantity_of_pages=book.quantity_of_pages,
            isbn=book.isbn,
        )
