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


def booking_report(request):
    booking_date = request.session['bookingDate']
    booking_set = Bookings.objects.filter(bookingDate=booking_date)
    print(booking_date)
    print(booking_set)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('occupancy from ' + str(booking_date))
    ws.write(0, 0, 'booking id')
    ws.write(0, 1, 'customer')
    ws.write(0, 2, 'date')
    ws.write(0, 3, 'length')
    ws.write(0, 4, 'date created')
    test = 0
    for i, booking in enumerate(booking_set):
        ws.write(i + 1, 0, str(Bookings.id))
        ws.write(i + 1, 2, str(Bookings.BookingId))
        ws.write(i + 1, 1, str(Bookings.user))
        ws.write(i + 1, 3, str(Bookings.bookingDate))
        ws.write(i + 1, 4, str(Bookings.bookingType))
        ws.write(i + 1, 5, str(Bookings.bookingPayment))
        ws.write(i + 1, 6, str(Bookings.seatsChosen))
        test = i
    ws.write(test + 2, 0, str(booking_set.count()))
    wb.save('C:/Users\Marc\Desktop\django_reports' + 'occupancy ' + 'date'
            + str(booking_date) + '.xls')
    del request.session['bookingDate']
    del request.session['occupancy']
    return



