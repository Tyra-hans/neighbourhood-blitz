from django.shortcuts import render,redirect
from django.contrib.auth import login
from .models import Post, Profile, Business, Neighbourhood
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UploadPostForm , UpdateProfileForm 


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

def business(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
        business = Business.objects.get(id = id)
   
    return render(request, 'all-posts/s_business.html', {'business': business})

def search(request):
    if 'site' in request.GET and request.GET['site']:
        search_term = request.GET.get('site')
        businesses = Business.objects.filter(title__icontains = search_term)
        message = f'{search_term}'
        return render(request, 'all-posts/search.html', {'businesses': businesses, 'message': message})
        
    return render(request, 'all-posts/search.html')

@login_required(login_url='/accounts/login/')
def create_post(request):
    if request.method == 'POST':
        form = UploadPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('home')
    else:
        form = UploadPostForm()

    return render(request, 'all-posts/create_post.html', {'form': form})
