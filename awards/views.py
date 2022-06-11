from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
import datetime as dt
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    date = dt.date.today()
    

    return render(request, 'main/index.html', {"date": date})


def register(request):             
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('/')
        
    else:
        form = RegisterForm()
    return render(request, 'registration/registration_form.html', {'form':form})


@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'users/profile.html')