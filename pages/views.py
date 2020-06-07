from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Profile, Contact

# Create your views here.
@login_required
def index_view(request):
    profile = Contact.objects.filter(user_from=request.user)
    context = {
        'profile' : profile,
    }
    return render(request, 'pages/index.html', context)
