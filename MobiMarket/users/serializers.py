from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=15, min_length=8)
    password_confirm = serializers.CharField(write_only=True, max_length=15, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def save(self):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'])
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if not user.username.isalnum():
            raise serializers.ValidationError("Username must consist of letters and numbers only.")

        if password != password_confirm:
            raise serializers.ValidationError("Passwords do not match.")
        user.set_password(password)
        user.save()


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=15, min_length=8, write_only=True)
    tokens = serializers.SerializerMethodField

    class Meta:
        model = User
        fields = ['username', 'password', 'tokens']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')

        user = auth.authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credential, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        return {
            'username': user.username,
            'tokens': user.tokens()
        }


class ProfileRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['avatar', 'username', 'email', 'first_name', 'last_name', 'date_of_birth']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()

        return instance


class CodeSendSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number']

    def update(self, instance, validated_data):
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance


class CodeCheckSerializer(serializers.Serializer):
    verification_code = serializers.CharField(max_length=6)

    class Meta:
        model = User
        fields = ['verification_code']
        read_only_fields = ['phone_number']
