from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from books.dtos import CreateBookDto
from books.forms import BookForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from books.models import Book
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from django.views.generic import FormView, DetailView, UpdateView, ListView
from books.pagination import BookPagination
from books.serializers import BookSerializer
from books.services import CreateBookService


class CreateListBookAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer
    pagination_class = BookPagination
    
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        
        input_validation_has_failed = not serializer.is_valid()
        
        if input_validation_has_failed:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = request.user

        create_book_dto = CreateBookDto(
            name=serializer.validated_data['name'],
            quantity_of_pages=serializer.validated_data['quantity_of_pages'],
            user=user
        )

        CreateBookService().execute(create_book_dto)

        return Response(
            status=status.HTTP_201_CREATED,
        )


class RetrieveUpdateDestroyBookApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


class CreateBookView(LoginRequiredMixin, FormView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("books")
    template_name = "create_book.html"

    def form_valid(self, form):
        user = self.request.user

        create_book_dto = CreateBookDto(
            name=form.cleaned_data["name"],
            quantity_of_pages=form.cleaned_data["quantity_of_pages"],
            user=user
        )

        try:
            CreateBookService().execute(create_book_dto)
        except Exception as exception:
            stringified_exception = str(exception)
            field_name = None

            form.add_error(field_name, stringified_exception)

            return self.form_invalid(form)

        success_message = 'Book registered with success'

        messages.success(self.request, success_message)

        success_redirect_url = self.get_success_url()

        return redirect(success_redirect_url)


class ListBookView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'list_books.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)
    

class DetailBookView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'detail_book.html'
    context_object_name = 'book'

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


class UpdateBookView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'update_book.html'
    context_object_name = 'book'
    success_url = reverse_lazy('books')

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Book updated successfully.")
        return super().form_valid(form)
