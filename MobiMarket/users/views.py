from rest_framework import generics, exceptions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User
import random
from django.conf import settings
from twilio.rest import Client
from .serializers import (RegistrationSerializer,
                          LoginSerializer,
                          ProfileRegistrationSerializer,
                          CodeSendSerializer,
                          CodeCheckSerializer)


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status.HTTP_200_OK)


class ProfileUpdateView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileRegistrationSerializer

    def put(self, request):
        user = request.user

        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CodeSendView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CodeSendSerializer

    def put(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        verification_code = ''.join(random.choice('0123456789') for _ in range(4))
        User.objects.update(
            phone_number=phone_number,
            verification_code=verification_code
        )
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        try:
            message = client.messages.create(
                body=f'Your verification code is: {verification_code}',
                from_=settings.TWILIO_PHONE_NUMBER,
                to=phone_number
            )
            return Response({'message': 'Verification code sent successfully.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': 'Failed to send verification code.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CodeCheckView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CodeCheckSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        verification_code = serializer.validated_data['verification_code']
        code = User.objects.filter(verification_code=verification_code).first()
        user = request.user

        if not user:
            raise exceptions.APIException('User not found!')

        if not code:
            raise exceptions.APIException('Code is incorrect!')

        user.is_verified = True
        user.save()
        return Response({
            'message': 'You successfully verified your phone number'
        })
