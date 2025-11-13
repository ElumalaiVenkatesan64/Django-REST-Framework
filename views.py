from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        phone = request.data.get('phone')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({
                "Message": "Username Already Exists!"
            }, status=status.HTTP_208_ALREADY_REPORTED)

        if User.objects.filter(email=email).exists():
            return Response({
                "Message": "Email ID Already Exists!"
            }, status=status.HTTP_208_ALREADY_REPORTED)

        else:
            new_user = User.objects.create_user(
                username=username,
                email=email,
                phone=phone,
                password=password

            )

            return Response({
                "Message": "New User Successfully Created",
            })


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user_verification = authenticate(
            username=username,
            password=password
        )

        if user_verification is not None:
            login(request, user_verification)
            refresh = RefreshToken.for_user(user_verification)
            return Response({
                "Refresh": str(refresh),
                "Access": str(refresh.access_token)
            })
        else:
            return Response({
                "Message": "Invalid Username or Password, Please try again!"
            })


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfile_Serializer(request.user)

        return Response(serializer.data)

    def patch(self, request):
        serializer = UserProfile_Serializer(
            request.user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "Message": "Deatails Successfully Updated",
                "Updated Data": serializer.data
            })

    def delete(self, request):
        user = request.user
        user.delete()

        return Response("User Data Deleted")
