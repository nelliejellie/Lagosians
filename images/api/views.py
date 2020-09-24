from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from ..models import Image, Comment
from .serializers import ImageSerializer, CommentSerializer


@csrf_exempt
def image_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        image = Image.objects.all()
        serializer = ImageSerializer(image, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)