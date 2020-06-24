from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Profile, Contact
from images.models import Image
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm

# Create your views here.
@login_required
def index_view(request):
    image = Image.objects.order_by('-created')
    profile = Contact.objects.filter(user_from=request.user)
    context = {
        'profile' : profile,
        'image' : image,
    }
    return render(request, 'pages/index.html', context)

def image_search(request):
    queryset_list = Image.objects.order_by('-created')
    if 'name' in request.GET:
        name = request.GET['name']
        print (name)
        if name:
            queryset_list = queryset_list.filter(title__icontains=name)
    context = {
        'posts': queryset_list,
        'values': name,
    }
    return render(request, 'pages/search.html', context)
