from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
    UserListSerializer
)

User = get_user_model()
CustomUser = User


class UserRegistrationView(generics.CreateAPIView):
    """View for user registration."""
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)
        return Response({
            'user': UserProfileSerializer(user).data,
            'token': token.key,
            'message': 'User registered successfully.'
        }, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    """View for user login."""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': UserProfileSerializer(user).data,
                'token': token.key,
                'message': 'Login successful.'
            }, status=status.HTTP_200_OK)
        return Response({
            'error': 'Invalid credentials.'
        }, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileView(generics.RetrieveUpdateAPIView):
    """View for retrieving and updating user profile."""
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserListView(generics.ListAPIView):
    """View for listing all users."""
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticated]


class FollowUserView(generics.GenericAPIView):
    """View for following a user."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)

        if user_to_follow == request.user:
            return Response({
                'error': 'You cannot follow yourself.'
            }, status=status.HTTP_400_BAD_REQUEST)

        if request.user in user_to_follow.followers.all():
            return Response({
                'error': 'You are already following this user.'
            }, status=status.HTTP_400_BAD_REQUEST)

        user_to_follow.followers.add(request.user)
        return Response({
            'message': f'You are now following {user_to_follow.username}.'
        }, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    """View for unfollowing a user."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)

        if user_to_unfollow == request.user:
            return Response({
                'error': 'You cannot unfollow yourself.'
            }, status=status.HTTP_400_BAD_REQUEST)

        if request.user not in user_to_unfollow.followers.all():
            return Response({
                'error': 'You are not following this user.'
            }, status=status.HTTP_400_BAD_REQUEST)

        user_to_unfollow.followers.remove(request.user)
        return Response({
            'message': f'You have unfollowed {user_to_unfollow.username}.'
        }, status=status.HTTP_200_OK)
