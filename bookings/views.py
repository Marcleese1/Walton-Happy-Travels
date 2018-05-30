from django.views.generic import TemplateView
from users.models import Customer
from django.shortcuts import render
from.models import Bookings
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from. import models
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    model = Customer
    template_name = 'home.html'


#gives the ability for staff to view all bookings
#and customers to view the bookings they have made
def view_bookings(request):
    if request.user.is_staff is True:
        query_results = Bookings.objects.all()
        context = {"query_results": query_results}
    else:
        query_results = Bookings.objects.filter(user=request.user)
        context = {"query_results": query_results}
    return render(request, 'bookings/bookings_list.html', context)


#this functions gives the ability to edit bookings already made
class EditBooking(UpdateView, LoginRequiredMixin):
    model = models.Bookings
    template_name = 'bookings/view_bookings.html'
    fields = ['seatsChosen']
    success_url = reverse_lazy('home')




