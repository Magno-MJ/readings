from abc import ABC, abstractmethod
from src.domain.entities.book import Book


class BookRepository(ABC):
    @abstractmethod
    def find_by_isbn(self, isbn: str) -> Book:
        pass

    @abstractmethod
    def save(self, book: Book):
        pass
