from rest_framework import status, generics, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Patient, Doctor
from .serializers import (
    UserSignupSerializer, 
    UserLoginSerializer, 
    UserDashboardSerializer
)
from .filters import UserFilter


@api_view(['POST'])
@permission_classes([AllowAny])
def signup_view(request):
    """User signup endpoint"""
    serializer = UserSignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'message': 'User registered successfully',
            'user': UserDashboardSerializer(user).data,
            'token': token.key,
            'user_type': user.user_type
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """User login endpoint"""
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'message': 'Login successful',
            'user': UserDashboardSerializer(user).data,
            'token': token.key,
            'user_type': user.user_type,
            'redirect_url': f'/api/{user.user_type}/dashboard/'
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def patient_dashboard(request):
    """Patient dashboard endpoint"""
    # Check if user is authenticated
    if not request.user.is_authenticated:
        return Response(
            {'error': 'Authentication required.'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    # Case-insensitive check for patient user_type
    user_type = getattr(request.user, 'user_type', '').lower()
    if user_type != 'patient':
        return Response(
            {
                'error': 'Access denied. Patient access required.',
                'current_user_type': request.user.user_type,
                'username': request.user.username
            },
            status=status.HTTP_403_FORBIDDEN
        )
    
    serializer = UserDashboardSerializer(request.user)
    return Response({
        'message': 'Welcome to Patient Dashboard',
        'user_data': serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def doctor_dashboard(request):
    """Doctor dashboard endpoint"""
    # Check if user is authenticated and has doctor user_type
    if not request.user.is_authenticated:
        return Response(
            {'error': 'Authentication required.'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    # Case-insensitive check for doctor user_type
    user_type = getattr(request.user, 'user_type', '').lower()
    if user_type != 'doctor':
        return Response(
            {
                'error': 'Access denied. Doctor access required.',
                'current_user_type': request.user.user_type,
                'username': request.user.username
            },
            status=status.HTTP_403_FORBIDDEN
        )
    
    serializer = UserDashboardSerializer(request.user)
    return Response({
        'message': 'Welcome to Doctor Dashboard',
        'user_data': serializer.data
    }, status=status.HTTP_200_OK)


class UserListView(generics.ListAPIView):
    """List all users with filtering"""
    queryset = User.objects.all()
    serializer_class = UserDashboardSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = UserFilter
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering_fields = ['created_at', 'username']
    ordering = ['-created_at']

