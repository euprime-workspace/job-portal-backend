from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *


class CreateProfile(generics.CreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


@api_view(['POST'])
def signUp(request):
    if request.method == 'POST':


        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
                serializer.save()
                return Response({'action': "Add New User", 'message': "User Added Successfully"},
                                status=status.HTTP_200_OK)
            else:
                return Response({'action': "Add User", 'message': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'action': "Add User", 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    print(request.data)
    try:
        username = request.data['username']
        password = request.data['password']
        user = get_object_or_404(CustomUser, username=username)

        if check_password(password, user.password):

            return Response({
                'action': "Login",
                'message': "Login Successful",
                'data': {
                    'id': user.id
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response({'action': "Login", 'message': "Incorrect Password"}, status=status.HTTP_401_UNAUTHORIZED)

    except Http404:
        return Response({'action': "Get Login", 'message': 'User Not Found'},
                        status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'action': "Get Login", 'message': str(e)},
                        status=status.HTTP_400_BAD_REQUEST)
