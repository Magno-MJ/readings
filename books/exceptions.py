from rest_framework.exceptions import APIException
from rest_framework import status

class BookAlreadyExistsException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Book already exists'
    default_code = 'book_already_exists'