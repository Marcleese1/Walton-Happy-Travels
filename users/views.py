# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import UserCustomerForm, UserChangeForm, CustomerChangeFormAdmin
from .models import Customer


class SignUp(generic.CreateView):
    form_class = UserCustomerForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

