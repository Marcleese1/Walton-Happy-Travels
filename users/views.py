# users/views.py
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import render, redirect
from .forms import UserCustomerForm, UserChangeForm, CustomerChangeFormAdmin
from .models import Customer
from django.contrib.auth.decorators import login_required
from .forms import DeactivateUserForm
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from setuptools import setup

version=__import__('social_auth').__version__


class SignUp(generic.CreateView):
    form_class = UserCustomerForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


#allows the user to delete their account
login_required(login_url= '/registration/login')


#def delete_user(request):
 #   Customer.objects.get(user=request.id).delete()
  #  Customer.objects.filter(pk=request.user.pk).update(is_active=False, email=None)
   # return HttpResponseRedirect(reverse('django.contrib.auth.views.logout'))
#

def edit(request):
    # allows the user to Edit their details
    if request.method =='POST':
        form = CustomerChangeFormAdmin(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerChangeFormAdmin(instance=request.user)
        args = {'form': form}
        return render(request, 'editdetails.html', args)
