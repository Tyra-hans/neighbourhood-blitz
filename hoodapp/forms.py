from django import forms
from .models import RegularProfile, User, AdminProfile 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')

class RegularProfileForm(forms.ModelForm):
    class Meta:
        model = RegularProfile
        fields = ('location', 'bio')
        
class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ('location', 'bio')