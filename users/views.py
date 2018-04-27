# users/views.py
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserCustomerForm


class SignUp(generic.CreateView):
    form_class = UserCustomerForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
