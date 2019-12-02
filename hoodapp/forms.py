from django import forms
from .models import Post, Neighbourhood, Profile, Business

class UploadPostForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['publish_date']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
