from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Customer
from django.shortcuts import render
from.models import Bookings
from. import models
from .forms import EditBookingForm, ChooseSeatsForm
from django.shortcuts import redirect
from packages.models import Packages
from django.http import HttpResponse


#displays the homepage
class HomePageView(TemplateView):
    model = Customer
    template_name = 'home.html'


#gives the ability for staff to view all bookings
#and customers to view the bookings they have made
def view_bookings(request):
    #if statement to check if user is staff and show all bookings
    if request.user.is_staff is True:
        query_results = Bookings.objects.all()
        context = {"query_results": query_results}
   #if the user is not staff it will get the user and display only the bookings they have made
    else:
        query_results = Bookings.objects.filter(user=request.user)
        context = {"query_results": query_results}
    return render(request, 'bookings/bookings_list.html', context)


#this functions gives the ability to edit bookings already made
class EditBooking(UpdateView, LoginRequiredMixin):
    queryset = models.Bookings.objects.all()
    template_name = 'bookings/view_bookings.html'
    form_class = EditBookingForm
    success_url = reverse_lazy('bookings_list')


#allows the user to delete their account
#class delete_booking(DeleteView):
 #   model = Bookings
  #  queryset = models.Bookings.objects.all()

   # def addquantity(self, form: ChooseSeatsForm):
    #    form.cleaned_data['quantity'] += form.instance.seatsChosen
     #   form.instance.save()
      #  return redirect('bookings_list')






