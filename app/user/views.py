from rest_framework import generics

from user.serlializers import UserSerializer


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
