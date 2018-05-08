from django.views.generic import TemplateView
from users.models import Customer
from users.views import CustomerChangeFormAdmin
from django.shortcuts import render, redirect
#from .forms import EditForm


class HomePageView(TemplateView):
    model = Customer
    template_name = 'home.html'


#def edit(request):
    #if request.method == 'post':
        #form = CustomerChangeForm(request.POST)
        #if form.is_valid():
          #  cust = Customer.objects.get(email=request.Customer.email, first_name=request.Customer.FirstName,
                                      #  last_name=request.Customer.LastName,
                                       # address_line1=request.Customer.Address_Line_1,
                                      #  address_line2=request.Customer.Address_Line_2,
                                      #  postcode=request.Customer.postcode,
                                       # town=request.Customer.town, homePhone=request.Customer.homePhone,
                                      #  PhoneNumber=request.Customer.PhoneNumber)
           # return redirect('home')
   # else:
      #  form = CustomerChangeForm()
   # return render(request, 'editdetails.html', {'form':form})
