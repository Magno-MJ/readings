from src.application.use_cases.create_book_use_case import CreateBookUseCase
from src.infra.database.repositories.book_repository import (
    DjangoBookRepository
)


class BookContainer:
    @staticmethod
    def create_book_use_case():
        repository = DjangoBookRepository()

        return CreateBookUseCase(repository)
