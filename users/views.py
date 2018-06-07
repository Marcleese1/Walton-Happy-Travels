# users/views.py
from django.shortcuts import render, redirect
from .forms import UserCustomerForm, CustomerChangeFormAdmin
from django.contrib.auth import login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.views.generic.edit import CreateView

version=__import__('social_auth').__version__


#sign up page for the user
class SignUp(CreateView):
    form_class = UserCustomerForm
    template_name = 'signup.html'
    success_url = 'login'



#allows the user to delete their account
def delete_account(request):
    cust = request.user
    cust.delete()
    logout(request)
    messages.add_message(request, messages.INFO, 'Customer successfully deleted')
    return render(request, 'home.html')


def edit(request):
    # allows the user to Edit their details
    if request.method == 'POST':
        form = CustomerChangeFormAdmin(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerChangeFormAdmin(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/editdetails.html', args)


#allows the customer to change their password
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'password.html', {'form': form})

