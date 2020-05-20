from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from bookmarks.common.decorators import ajax_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

# Create your views here.
@login_required
def image_create(request):
    if request.method == 'POST':
        #form is sent
        form = ImageCreateForm(data=request.POST or None, files=request.FILES)
        print(request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            #assign current user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Images added successful')
            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        #build form with data provided by the bookmarklet via get
        form = ImageCreateForm()

    context = {
        'section' : 'images',
        'form' : form
    }
    return render (request, 'images/image/create.html', context)

def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    context = {
        'section' : 'images',
        'image' : image,
    }
    return render(request, 'images/image/detail.html', context)

@login_required
@require_POST
@ajax_required
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    print(request.POST)
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
                return JsonResponse({'status':'ok'})
        except:
            pass
        return JsonResponse({'status':'error'})

@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # If the request is AJAX and the page is out of range
            # return an empty page
            return HttpResponse('')
        # If page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        context = {
            'section' : 'images',
            'images' : images,
        }
        return render (request, 'images/image/list_ajax.html', context)
    context = {
            'section' : 'images',
            'images' : images,
        }
    return render(request, 'images/image/list.html', context)