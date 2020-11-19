from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.api.serializers import RegisterationSerializer,AccountSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes, renderer_classes



# make sure the function only accepts post request
@api_view(['POST',])
def registeration_view(request):
    serializer = RegisterationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'successfully registered'
        data['email'] = account.email
        data['username'] = account.username
        # get the token of the new user 
        token = Token.objects.get(user=account).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data)

@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def account_properties_view(request):
    try:
        user = request.user
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = AccountSerializer(user)
    return Response(serializer.data)

@api_view(['PUT',])
@permission_classes([IsAuthenticated,])
def account_update_view(request):
    try:
        user = request.user
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = AccountSerializer(user, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Account was updated successfully'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)