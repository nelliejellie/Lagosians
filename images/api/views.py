from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
# for user permissions and authentication
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from ..models import Image, Comment
from .serializers import ImageSerializer, CommentSerializer
from django.contrib.auth.models import User
# for user permissions and authentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
# for pagination
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


# paginated list of images
@api_view(['GET',])
@permission_classes([AllowAny,])
@csrf_exempt
def image_list_view(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 1
        person_objects = Image.objects.all()
        result_page = paginator.paginate_queryset(person_objects, request)
        serializer = ImageSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

# list of all images
@csrf_exempt
@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def image_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        image = Image.objects.all()
        serializer = ImageSerializer(image, many=True)
        return JsonResponse(serializer.data, safe=False)
        
        
# post image function
# using the decorator to allow only post requests    
@api_view(['POST',])
def post_image_list(request):
    user = User.objects.get(pk=request.user.id)
    image = Image(user=user)
    serializer = ImageSerializer(image, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# delete image function
# for deleting your own personal post
@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def image_list_delete(request, slug):
    try:
        image = Image.objects.get(slug=slug)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        operation = image.delete()
        data = {}
        if operation:
            data['success'] = 'delete successful'
        else:
            data['failure'] = 'delete failed'
        return Response(data=data)

@permission_classes((AllowAny,))
def image_list_detail(request, slug):
    try:
        image = Image.objects.get(slug=slug)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ImageSerializer(image)
        return JsonResponse(serializer.data)

# class based view to get the list of images
# class ApiImageListView(ListAPIView, BrowsableAPIRenderer): 
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     pagination_class = PageNumberPagination()



        
    

    

