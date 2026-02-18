from rest_framework import serializers


class CreateUserSerializer(serializers.Serializer):
  first_name = serializers.CharField(max_length=180, required=True)
  last_name = serializers.CharField(max_length=100, required=True)
  email = serializers.EmailField()
  password = serializers.CharField(max_length=300, required=True)