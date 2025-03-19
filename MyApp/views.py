from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.shortcuts import get_object_or_404

# User Registration API
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login API
class LoginView(APIView):
    throttle_classes = [AnonRateThrottle] 
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = CustomUser.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)
    def get (self,request,pk):
        user=get_object_or_404(CustomUser,pk=pk)
        serializer=UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)