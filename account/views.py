from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm,UserEditForm,ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Contact
from django.contrib import messages
from django.contrib.auth.models import User
from bookmarks.common.decorators import ajax_required
from django.views.decorators.http import require_POST
from actions.utils import create_action
from actions.models import Action 



# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #to check if the username and password is in the database
            user = authenticate(request, username=cd['username'],password=cd['password'])
            if user is not None :
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated Successfully')

                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    #display all actions by default
    actions = Action.objects.exclude(user=request.user)
    following_ids = request.user.following.values_list('id', flat=True)

    if following_ids:
        #if users is following others, retrive only their actions
        actions = actions.filter(user_id__in = following_ids)
    # get the first 10 actions perfomerd by the user
    actions = actions.select_related('user', 'user__profile').prefetch_related('target')[:10]
    context = {
        'section' : 'dashboard',
        'actions' : actions,
        }
    return render(request, 'account/dashboard.html', context)

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid(): #add another condition to check if its lagos
        #create a new user but avoid saving it yet        
            new_user = user_form.save(commit=False)
        #set the choosen password
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            #create the user profile
            Profile.objects.create(user=new_user)
            create_action(new_user, 'has created an account')
            return render (request, 'account/register_done.html', {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required #user must be logged in before accessing this view
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST or None)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST or None,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(request, 'profile updated successfully')
        else:
            messages.error(request, 'An error occurred while trying to update your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form':profile_form})

@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    context = {
        'section':'people',
        'users': users,
    }
    return render(request, 'account/user/list.html', context)

@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    context = {
        'section':'people',
        'user': user,
    }
    return render (request, 'account/user/detail.html', context)

@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user, user_to=user)
                create_action(request.user, 'is following', user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse ({'status':'error'})
    return JsonResponse ({'status':'error'})

