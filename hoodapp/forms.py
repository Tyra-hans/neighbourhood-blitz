from django import forms
from .models import RegularProfile, User, AdminProfile 
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class InternProfileForm(forms.ModelForm):
    class Meta:
        model = RegularProfile
        fields = ('location', 'bio')
        
class HRProfileForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ('location', 'bio')