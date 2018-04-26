# posts/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.urls import reverse_lazy
#from django.http import Http404
from django.views.generic import TemplateView
#from .models import Bookings
from users.models import Customer
from . import models


class HomePageView(TemplateView):
    model = Customer
    template_name = 'home.html'
    login_url = 'login'

#class BookingHome(LoginRequiredMixin, ListView):
  #  model = models.Bookings

   # template_name = 'home.html'
    #login_url = 'login'

