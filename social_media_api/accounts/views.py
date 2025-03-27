from django.shortcuts import render
from .serializers import CustomUserSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User  # ✅ 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import generics 
from rest_framework import permissions



# ✅ Fixed RegisterUserView
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Fixed LoginView
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# ✅ Fixed ProfileView
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        """Follow another user"""
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            request.user.following.add(user_to_follow)
            return Response({"message": "You are now following this user."}, status=200)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=404)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        """Unfollow a user"""
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
            request.user.following.remove(user_to_unfollow)
            return Response({"message": "You have unfollowed this user."}, status=200)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=404)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    try:
        user_to_follow = CustomUser.objects.get(id=user_id)
        request.user.following.add(user_to_follow)  # ✅ Add follow relationship
        return Response({"message": "Followed successfully"}, status=200)
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = CustomUser.objects.get(id=user_id)
        request.user.following.remove(user_to_unfollow)  # ✅ Remove follow relationship
        return Response({"message": "Unfollowed successfully"}, status=200)
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found"}, status=404)