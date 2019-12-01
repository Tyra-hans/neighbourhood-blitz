from django.shortcuts import render,redirect
from django.contrib.auth import login
from .models import User

def intern_profile_view(request):
	
    if request.method == 'POST':
		
        user_form = UserForm(request.POST, prefix='UF')
        profile_form = RegularProfileForm(request.POST, prefix='PF')
		
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            user.regular_profile.bio = profile_form.cleaned_data.get('bio')
            user.regular_profile.location = profile_form.cleaned_data.get('location')
            user.regular_profile.save()
			
        else:
            user_form = UserForm(prefix='UF')
            profile_form = RegularProfileForm(prefix='PF')
		
    return render(request, 'regular/reg_profile.html', {'user_form': user_form,'profile_form': profile_form})

def landing(request):
    return render(request,'all-posts/landing.html')

def home(request):
    return render(request, 'all-posts/home.html')
