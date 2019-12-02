from django.shortcuts import render,redirect
from django.contrib.auth import login
from .models import Post, Profile, Business, Neighbourhood
from django.contrib.auth.models import User


def landing(request):
    return render(request,'all-posts/landing.html')

def home(request):
    return render(request, 'all-posts/home.html')

def profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    posts = Post.objects.filter(user = user)
    return render(request, 'all-posts/profile.html', {'profile': profile, 'posts': posts})

# @login_required(login_url='/accounts/login')
def update_profile(request):
    
    my_prof = Profile.objects.get(user=request.user)
    form = UpdateProfileForm(instance=request.user)
   