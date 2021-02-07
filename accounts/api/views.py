from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status, views, permissions
from .serializers import ResetPasswordEmailRequestSerializer
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError

from django.contrib.auth.tokens import PasswordResetTokenGenerator



jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

# @csrf_exempt
class AuthView(APIView):
    # building custom view for login and counting login times
    permission_classes=[permissions.AllowAny]
    def post(self, request,*args, **kwargs):
        if request.user.is_authenticated():
            return Response({'detail':'you are already logged in.'} , status = 400)
        if request.session.get('count', 0) == 0:
            request.session['count'] = 1
        else:
            request.session['count'] += 1

            if request.session['count'] == 3:
                pass
                # add user to blacklist    


        data = request.data
        print(data)
        username = data.get['username']
        password = data.get['password']
        print(username)
        user = authenticate(username=username , password=password)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        response = jwt_response_payload_handler(token , user , request=request)
        print(response)
        return Response(response)




class RequestPasswordResetEmail(generics.GenericAPIView):
    # creating pin for reset password 
    serializer_class = ResetPasswordEmailRequestSerializer
    permission_classes=[permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')
        print(email)
        # if user exist we are creating a unique token using tokengenerator
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            return Response({"message": "Forget email sent successfully","forget_pin":token,"status": 1,}, status=status.HTTP_200_OK)
        return Response({'failure': 'email not found',"status": 0,})



class PasswordTokenCheckAPI(generics.GenericAPIView):
    permission_classes=[permissions.AllowAny]   
    def post(self, request):
        # here we are accepting the pin and if pin is correct changing password
        verify_pin = request.data.get('verify_pin', '')
        password = request.data.get('password', '')
        confirm_password = request.data.get('confirm_password', '')
        email = request.data.get('email', '')
        if User.objects.filter(email=email).exists():
            if password != confirm_password:
                return Response({"message": "Password reset not successfull",'status':2})
            user = User.objects.get(email=email)
            if  PasswordResetTokenGenerator().check_token(user, verify_pin):

                return Response({"message": "Password reset successfully",'status':1,})
        return Response({"message": "Password reset not successfull",'status':0})
         