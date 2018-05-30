# users/views.py
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import render, redirect
from .forms import UserCustomerForm, UserChangeForm, CustomerChangeFormAdmin
from django.contrib.auth import login, logout

version=__import__('social_auth').__version__


class SignUp(generic.CreateView):
    form_class = UserCustomerForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


#allows the user to delete their account
def delete_account(request):
    cust = request.user
    cust.delete()
    logout(request)
    return render(request, 'home.html')


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


