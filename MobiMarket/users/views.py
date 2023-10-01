from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import exceptions
from .models import User
from .serializers import (RegistrationSerializer, LoginSerializer, ProfileRegistrationSerializer,
                          CodeSendSerializer, CodeCheckSerializer, LogoutSerializer, ProfileSerializer)
import random
from django.conf import settings
from twilio.rest import Client


def custom_swagger_auto_schema(description, response=None, tags=None):
    """
    Общая функция для создания аннотаций OpenAPI
    """
    return swagger_auto_schema(
        operation_description=description,
        responses={200: response} if response else None,
        tags=tags
    )


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    @custom_swagger_auto_schema(
        description="Register a new user",
        response=openapi.Response("User registration data"),
        tags=["Authentication"]
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


# Повторите тот же подход для других представлений...

class LogoutView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = LogoutSerializer

    @custom_swagger_auto_schema(
        description="Logout the user",
        response=openapi.Response("Logout response"),
        tags=["Authentication"]
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
