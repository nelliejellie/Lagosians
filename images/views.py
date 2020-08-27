from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm, CommentForm
from .models import Image, Comment
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from bookmarks.common.decorators import ajax_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from actions.utils import create_action
import redis
from django.conf import settings
from django.contrib.postgres.search import SearchVector


#redis initialization
r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

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
            create_action(request.user, 'uploaded image', new_item)
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
    images = get_object_or_404(Image, id=id, slug=slug)
    # increment total image views by 1 using redis
    total_views = r.incr(f'image:{images.id}:views')
    # increment total image views by 1 using redis
    r.zincrby('image_ranking', 1, images.id)

    # add comments to the view
    comments = images.images_comment.filter(active=True)
    # instantiate a new comment
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            cd = comment_form.cleaned_data
            # create a comment object but dont save to the database yet
            new_comment = comment_form.save(commit=False)
            # assign the current post to the comment
            new_comment.image = images
            new_comment.user = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    for comment in comments:
        if request.method == 'POST':
            if request.POST.get('like') == str(comment.id):
                print(f'{request.user} liked {comment.body} and this is the {comment.id}')
                comment.like.add(request.user)
                comment.count_like = str(comment.like.count)
                comment.save()
    context = {
        'section' : 'images',
        'image' : images,
        'total_views' : total_views,
        'comments': comments,
        'comment_form': comment_form,
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
                create_action(request.user, 'likes', image)
            else:
                image.users_like.remove(request.user)
                return JsonResponse({'status':'ok'})
        except:
            pass
        return JsonResponse({'status':'error'})

@login_required
def image_list(request):
    images = Image.objects.filter(user=request.user)
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

@login_required
def image_ranking(request):
    #get image ranking dictionary
    image_ranking = r.zrange('image_ranking', 0, -1, desc=True)[:10]
    image_ranking_ids = [int(id) for id in image_ranking]
    #get most viewed images
    most_viewed = list(Image.objects.filter(id__in=image_ranking_ids))
    most_viewed.sort(key=lambda x: image_ranking_ids.index(x.id))
    context = {
        'section' : 'images',
        'most_viewed' : most_viewed,
    }
    return render(request, 'images/image/ranking.html')


