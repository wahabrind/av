from rest_framework import serializers
from django.contrib.auth.models import User

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    confirm_password = serializers.CharField(
        min_length=1, write_only=True)
    verify_pin = serializers.CharField(
        min_length=1, write_only=True)
    email = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'confirm_password', 'verify_pin' , 'email']

    def validate(self, attrs):
        # try:
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        verify_pin = attrs.get('verify_pin')
        email = attrs.get('email')

        print(email)
        print(password)
        if password != confirm_password:
            raise serializers.ValidationError('passwords do not match', 401)
        # id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(email=email)
        if not PasswordResetTokenGenerator().check_token(user, verify_pin):
            raise serializers.ValidationError('The reset link is invalid', 401)

        user.set_password(password)
        user.save()
        return attrs

        return (user)
        # except Exception as e:
        #     raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)
