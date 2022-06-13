from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib import messages
import datetime as dt
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from .models import *
# from django.core.exceptions import ObjectDoesNotExist
import random


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    site = Sites.objects.all()
    now = dt.datetime.now().day
    date = dt.date.today()

    if request.method == "POST":
        form = NewSiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.user = request.user
            site.save()
    else:
        form = NewSiteForm()

    try:
        sites = Sites.objects.all()
        sites = sites[::-1]
        a_site = random.randint(0, len(sites)-1)
        random_site = sites[a_site]
        print(random_site.site_name)
    except Sites.DoesNotExist:
        raise Http404()

    return render(request, 'main/index.html', {'sites': sites, 'form': form, 'random_site': random_site, 'date':date, 'now':now})


# def register(request):             
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}')
#             return redirect('login')       
#     else:
#         form = RegisterForm()
#     return render(request, 'registration/registration_form.html', {'form':form})

def search(request):
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_sites = Sites.search_site(search_term)
        message = f"{search_term}"

        return render(request, 'main/search.html', {"message":message,"sites": searched_sites})

    else:
        message = ""
        return render(request, 'main/search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    author = current_user
    sites = Sites.get_by_author(author)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('users-profile')
        
    else:
        form = ProfileUpdateForm()
    
    return render(request, 'users/profile.html', {"form":form, "sites":sites})

@login_required(login_url='/accounts/login/')
def new_site(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewSiteForm(request.POST, request.FILES)
        if form.is_valid():
            site = form.save(commit=False)  # commit=False to avoid saving the model yet
            site.author = current_user
            site.save()                       # Save the model
        return redirect('index')

    else:
        form = NewSiteForm()
    return render(request, 'main/new-site.html', {"form": form})

@login_required(login_url='/accounts/login/')
def site_detail(request, id):
    try:
        site = Sites.objects.get(pk = id)
        
    except ObjectDoesNotExist:
        raise Http404()
    
    return render(request, 'main/site.html',{"site":site})

@login_required(login_url='/accounts/login/')
def tagged(request, tag):
    tag = get_object_or_404(Tag)
    # Filter sites by tag name  
    sites = Sites.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'sites':sites,
    }
    return render(request, 'main/index.html', context)