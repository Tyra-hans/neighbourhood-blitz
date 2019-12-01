from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic import CreateView

from .forms import RegularSignUpForm
from .models import User

class RegularSignUpView(CreateView):
    model = User
    form_class = RegularSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'regular'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('regulars')



