from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView
from users.models import Customer
from users.views import CustomerChangeFormAdmin
from django.shortcuts import render, redirect
from.models import Bookings


#class BookingViewMixin(object):
 #   model = Bookings, Customer
  #  form_class = BookingForm


class HomePageView(TemplateView):
    model = Customer
    template_name = 'home.html'


def edit(request):
    if request.method == 'post':
        form = CustomerChangeFormAdmin(request.POST)
        if form.is_valid():
            cust = Customer.objects.get(email=request.user.email, first_name=request.user.FirstName,
                                        last_name=request.user.LastName,
                                        address_line1=request.user.Address_Line_1,
                                        address_line2=request.user.Address_Line_2,
                                        postcode=request.user.postcode,
                                        town=request.user.town, homePhone=request.user.homePhone,
                                        PhoneNumber=request.user.PhoneNumber)
            return redirect('home')
    else:
        form = CustomerChangeFormAdmin()
    return render(request, 'editdetails.html', {'form':form})


def view_bookings(request):
    query_results = Bookings.objects.filter(user=request.user)
    context = {"query_results": query_results}
    return render(request, 'bookings/bookings_list.html', context)


def editbooking(request):
    # allows the user to Edit their details
    if request.method =='POST':
        form = CustomerChangeFormAdmin(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerChangeFormAdmin(instance=request.user)
        args = {'form': form}
        return render(request, 'editbooking.html', args)



