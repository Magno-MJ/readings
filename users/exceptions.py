from rest_framework.exceptions import APIException
from rest_framework import status

class UserAlreadyExistsException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'User already exists'
    default_code = 'user_already_exists'