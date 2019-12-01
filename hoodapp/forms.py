from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from hoodapp.models import Regular, User

class RegularSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_regular = True
        user.save()
        regular = Regular.objects.create(user=user)
        return user