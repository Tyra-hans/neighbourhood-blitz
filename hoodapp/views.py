from django.shortcuts import render,redirect
from django.contrib.auth import login
from .models import Post, Profile, Business, Neighbourhood
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def landing(request):
    return render(request,'all-posts/landing.html')

@login_required(login_url='/accounts/login/')
def home(request):
    context = {
        'posts': Post.objects.all(),
        
    }
    return render(request, 'all-posts/home.html', context)


def profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    posts = Post.objects.filter(user = user)
    return render(request, 'all-posts/profile.html', {'profile': profile, 'posts': posts})

# @login_required(login_url='/accounts/login')
def update_profile(request):
    
    my_prof = Profile.objects.get(user=request.user)
    form = UpdateProfileForm(instance=request.user)

def post(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
        post = Post.objects.get(id = id)
   
    return render(request, 'all-posts/s_post.html', {'post': post})


   