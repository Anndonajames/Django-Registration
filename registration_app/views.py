from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import User


def home(request):
    return render(request, 'registration_app/home.html')

def gallery(request):
    return render(request, 'registration_app/gallery.html')

def register(request):
 
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'registration_app/register.html',{'form':form})


@login_required()
def profile(request):
    current_user = request.user
    if request.user.is_superuser:
        users = User.objects.values()
        #messages.success(request, f'Hi {users}')
        print(users)
        
        #messages.success(request, f'Hi {current_user}, you are the super user')
    else:
        if request.user:
            users = User.objects.values()
        
    messages.success(request, f'Hi {current_user}, your profile Here')
    print(current_user)

    return render(request, 'registration_app/profile.html',{'objs':users})



    