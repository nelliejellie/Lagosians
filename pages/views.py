from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Profile, Contact
from images.models import Image

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
