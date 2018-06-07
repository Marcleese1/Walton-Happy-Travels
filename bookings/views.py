from .forms import EditBookingForm
from datetime import datetime, timedelta
import datetime

import xlwt
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Customer
from django.shortcuts import render, redirect
from.models import Bookings
from. import models
from .forms import GenerateReport
from packages.models import Packages


#displays the homepage
class HomePageView(TemplateView):
    model = Customer
    template_name = 'home.html'


#gives the ability for staff to view all bookings
#and customers to view the bookings they have made
def view_bookings(request):
    seats = request.GET.get('seatsChosen')
    #if statement to check if user is staff and show all bookings
    if request.user.is_staff is True:
        query_results = Bookings.objects.all()
        context = {"query_results": query_results}
   #if the user is not staff it will get the user and display only the bookings they have made
    else:
        query_results = Bookings.objects.filter(user=request.user)
        context = {"query_results": query_results}
    request.session['seatsChosen'] = seats
    return render(request, 'bookings/bookings_list.html', context)


#this functions gives the ability to edit bookings already made
class EditBooking(UpdateView, LoginRequiredMixin):
    queryset = models.Bookings.objects.all()
    template_name = 'bookings/view_bookings.html'
    form_class = EditBookingForm
    success_url = reverse_lazy('bookings_list')




