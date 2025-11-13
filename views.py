from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.permissions import IsAuthenticated
from .models import *

class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username Already exists"})
        
        else:
            new_user = User.objects.create_user(username=username, password=password)
            new_user.save()

            return Response("New User Register SuccessFully")
        

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
        
        else:
            return Response("Invald Username or Password. Please Try Again!")
        
    
        

class UserProfileAPIView(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request):
        user = request.user
        return Response({"Username": user.username, "Password": user.password})