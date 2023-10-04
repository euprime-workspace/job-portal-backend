from django.http import Http404
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Prefetch
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate

from .models import *
from .serializers import *


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CreateProfile(request):
    if request.method == 'POST':
        try:
            # Get the file data from the request
            file_data = request.FILES.get('fileInput')

            # Create the File instance and save the file data to it
            if file_data:
                file_serializer = FileSerializer(data={'uploaded_file': file_data})
                if file_serializer.is_valid():
                    file_instance = file_serializer.save()

            # Create the Profile instance with other data
            profile_serializer = ProfileSerializer(data=request.data)
            if profile_serializer.is_valid():
                # Get the validated data from the serializer
                profile_data = profile_serializer.validated_data

                # Create the Profile instance and set the resume field
                profile = Profile(**profile_data, resume=file_instance)
                profile.save()
                return Response({'action': "Add Profile", 'message': "Profile Added Successfully"},
                                status=status.HTTP_200_OK)
            else:
                return Response({'action': "Add Profile", 'message': profile_serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'action': "Add Profile", 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


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


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def login(request):
    try:
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)

        if user:
            # User authentication succeeded
            # refresh = RefreshToken.for_user(user)
            # access_token = str(refresh.access_token)

            return Response({
                'action': "Login",
                'message': "Login Successful",
                'data': {
                    'id': user.id,
                    # 'access_token': access_token,
                    # 'refresh_token': str(refresh),  # Include the refresh token
                }
            }, status=status.HTTP_200_OK)
        else:
            # User authentication failed
            return Response({'action': "Login", 'message': "Incorrect Password"}, status=status.HTTP_401_UNAUTHORIZED)

    except Http404:
        return Response({'action': "Get Login", 'message': 'User Not Found'},
                        status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'action': "Get Login", 'message': str(e)},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createRecruiter(request):
    if request.method == "POST":
        user = request.user
        # user=CustomUser.objects.get(id="58b383a9-f4e1-47ce-a0b1-8db5cb144f73")
        try:
            request.data['user'] = user.id
            serializer = RecruiterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'action': "Add New Recruiter", 'message': "Recruiter Added Successfully"},
                                status=status.HTTP_200_OK)
            else:
                return Response({'action': "Add Recruiter", 'message': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'action': "Add Recruiter", 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewRecruiter(request):
    user = request.user
    try:
        recruiter = Recruiter.objects.get(user=user)
        serializer = RecruiterViewSerializer(recruiter)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Recruiter.DoesNotExist:
        return Response({'error': 'Recruiter not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def googleLogin(request):
    try:
        username = request.data['username']
        if not CustomUser.objects.filter(username=username).exists():
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
                serializer.save()
                return Response({'action': "Add New User", 'message': "User Added Successfully"},
                                status=status.HTTP_200_OK)
            else:
                return Response({'action': "Add User", 'message': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'action': "User Already exits", 'message': "User already exits"},
                            status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'action': "Get Login", 'message': str(e)},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewCandidates(request):
    try:
        profiles = Profile.objects.all()
        serializer = ProfileViewSerializer(profiles, many=True)  # Provide the queryset as data
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': 'Something went wrong'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewCandidateProfile(request, id):
    try:
        profile = Profile.objects.select_related('user').get(user_id=id)
        serializer = ProfileViewSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': 'No such candidate exists'}, status=status.HTTP_404_NOT_FOUND)


def getUserId(request):
    try:
        username = request.data['username']
        user = CustomUser.objects.get(username=username)
        if user:
            return Response({'id': user.id, "userType": user.user_type}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': 'Something went wrong'}, status=status.HTTP_404_NOT_FOUND)
