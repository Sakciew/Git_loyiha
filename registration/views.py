from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from registration.forms import Custom_user_form


def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')

class SignUp(CreateView):
    form_class =Custom_user_form
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
