from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from hoodapp.models import Regular, User , Neighbourhood

class RegularSignUpForm(UserCreationForm):

    neighbourhood = forms.ModelMultipleChoiceField(
        queryset=Neighbourhood.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_regular = True
        user.save()
        regular = Regular.objects.create(user=user)
        regular.neighbourhoodss.add(*self.cleaned_data.get('neighbourhoods'))
        return user