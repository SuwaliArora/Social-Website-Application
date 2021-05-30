from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from common.decorators import ajax_required

# Create your views here.
def user_login(request):  #user login view is called with a get request
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): # check if form is valid or not
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            #authenticate the user against database using the authenticate() method
            if user is not None:
                if user.is_active:    #is_active is an attribute of django user model
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')

                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

#login_required decorator of the authentication framework.
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object but avoid saying it yet
            new_user = user_form.save(commit=False)
            #set the chosen password
            #set_password() method of user model that handles encrption to save for safety reasons.
            new_user.set_password(user_form.cleaned_data['password'])
            #save the user object
            new_user.save()
            Profile.objects.create(user=new_user)  #create the user profile
            return render(request, 'account/register_done.html', {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required  #login_required decorator because users have to be authenticated to edit their	profile.
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # add a	success	message	when the user successfully updates their profile.
            messages.success(request, 'Profile updated successfully')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def user_list(request):  # to get all active users
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/list.html', {'section': 'people', 'users': users})

@login_required
def user_detail(request, username):  # to retrieve the active user with given username
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section': 'people', 'user': user})
    
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
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'ko'})
    return JsonResponse({'status':'ko'})
