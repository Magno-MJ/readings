from src.application.use_cases.create_book_use_case import (
    BookAlreadyRegisteredException,
    CreateBookDto,
)
from src.infra.http.serializers.create_book_serializer import (
    CreateBookSerializer
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from src.infra.setup.containers.book import create_book_use_case


class CreateBookAPIView(APIView):
    def post(self, request):

        serializer = CreateBookSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            payload = serializer.validated_data

            name = payload.get("name")
            quantity_of_pages = payload.get("quantity_of_pages")
            isbn = payload.get("isbn")

            dto = CreateBookDto(
                name=name,
                quantity_of_pages=quantity_of_pages,
                isbn=isbn,
            )

            create_book_use_case.execute(dto)
        except BookAlreadyRegisteredException as exception:
            exception_message = str(exception)

            return Response(
                {"message": exception_message},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            status=status.HTTP_201_CREATED
        )
