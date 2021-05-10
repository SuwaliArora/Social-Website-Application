from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

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
