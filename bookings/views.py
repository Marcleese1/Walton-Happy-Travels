from django.views.generic import TemplateView
from users.models import Customer
from users.views import CustomerChangeFormAdmin
from django.shortcuts import render, redirect


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


#def ViewPreviousBookings(request, id):
