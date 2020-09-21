from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.api.serializers import RegisterationSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.authtoken.models import Token



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