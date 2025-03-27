from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import CustomUserSerializer, RegisterSerializer

# ✅ Register User View
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)  # Use correct serializer
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': CustomUserSerializer(user).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Login User View
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': CustomUserSerializer(user).data}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# ✅ Profile View
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Follow a User
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    """Allows an authenticated user to follow another user."""
    user_to_follow = get_object_or_404(CustomUser, id=user_id)

    if user_to_follow == request.user:
        return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.add(user_to_follow)  # ✅ Ensure "following" is ManyToManyField in CustomUser
    return Response({"message": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

# ✅ Unfollow a User
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    """Allows an authenticated user to unfollow another user."""
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

    if user_to_unfollow == request.user:
        return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.remove(user_to_unfollow)
    return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)
