from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from users.apis.serializers import RegistrationSerializer, ProfileSerializer
from rest_framework.authtoken.models import Token
from users.models import Profile
from django.contrib.auth.models import User


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'successfully registered a new user.'
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
    
    
# @api_view(['GET', 'PUT',])
# @permission_classes((IsAuthenticated,))
# def update_profile(request):
#     if request.method == 'PUT':
#         my_profile = Profile.objects.get(user=request.user)
#         serializer = ProfileSerializer(my_profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = Profile.objects.get(user=request.user)
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def update_profile(request):
    try:
        my_profile = Profile.objects.get(user=request.user)
    except my_profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # user = request.user
    # if my_profile.get_username != user:
    #     return Response({'response': "You don't have permission to edit that"})

    if request.method == 'PUT':
        serializer = ProfileSerializer(my_profile, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)