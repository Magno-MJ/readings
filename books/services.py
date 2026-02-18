from books.dtos import CreateBookDto
from books.exceptions import BookAlreadyExistsException
from books.models import Book

class CreateBookService():
    def execute(self, create_book_dto: CreateBookDto):
        book_name = create_book_dto.name
        user = create_book_dto.user

        book_already_exists = Book.objects.filter(name=book_name, user=user).exists()

        if book_already_exists:
            raise BookAlreadyExistsException()
        
        book = Book(
            name=create_book_dto.name,
            quantity_of_pages=create_book_dto.quantity_of_pages,
            user=user,
        )

        book.save()
