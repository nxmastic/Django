<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from .models import Account
from django.template import loader
from django.http import HttpResponse

# def login(request):
#     #

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/account/register')
    else:
        #
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)

# def logout(request):
#     #



# Create your views here.
=======
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from .models import Account
from django.template import loader
from django.http import HttpResponse

# def login(request):
#     #

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/account/register')
    else:
        #
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)

# def logout(request):
#     #



# Create your views here.
>>>>>>> 2480c54b8f7df51e28a370924a66f630a3ddc302
