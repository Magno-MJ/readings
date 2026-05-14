from rest_framework import serializers
from django.core.validators import MinValueValidator


class CreateBookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    quantity_of_pages = serializers.IntegerField(validators=[
        MinValueValidator(1)
    ])
    isbn = serializers.CharField()
