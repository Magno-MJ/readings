from rest_framework import generics
from django.views.generic.edit import FormView
from rest_framework import status
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from rest_framework.response import Response
from users.dtos import CreateUserDto
from users.forms import CreateUserForm
from users.serializers import CreateUserSerializer
from users.services import CreateUserService


class CreateUserAPIView(generics.CreateAPIView):
    def create(self, request):
        serializer = CreateUserSerializer(data=request.data)

        input_validation_has_failed = not serializer.is_valid()
        
        if input_validation_has_failed:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        create_user_dto = CreateUserDto(
            email=serializer.validated_data['email'],
            first_name=serializer.validated_data['first_name'],
            last_name=serializer.validated_data['last_name'],
            password=serializer.validated_data['password'],
        )

        CreateUserService().execute(create_user_dto)

        return Response(
            status=status.HTTP_201_CREATED,
        )


class CreateUserView(FormView):
    template_name = "create_user.html"
    form_class = CreateUserForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user_dto = CreateUserDto(
            email=form.cleaned_data["email"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            password=form.cleaned_data["password"],
        )

        try:
            CreateUserService().execute(user_dto)
        except Exception as exception:
            stringified_exception = str(exception)
            field_name = None

            form.add_error(field_name, stringified_exception)

            return self.form_invalid(form)

        success_message = 'User registered with success'

        messages.success(self.request, success_message)

        success_redirect_url = self.get_success_url()

        return redirect(success_redirect_url)
    

