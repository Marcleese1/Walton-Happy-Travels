# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import UserCustomerForm, UserChangeForm, CustomerChangeFormAdmin
from .models import Customer
from django.contrib.auth.decorators import login_required
from .forms import DeactivateUserForm
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied


class SignUp(generic.CreateView):
    form_class = UserCustomerForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


#allows the user to delete their account
login_required(login_url= '/registration/login')


def delete_user(request):
    pk = request.user.id
    user = Customer.objects.get(pk=pk)
    user_form=DeactivateUserForm(instance=user)
    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == "POST":
            user_form= DeactivateUserForm(request.POST, instance=user)
            if user_form.is_valid():
                deactivate_user = user_form.save(commit=False)
                user.is_active = False
                deactivate_user.save()
                return HttpResponseRedirect(reverse_lazy('account_logout'))
            return render(request, "registration/user_delete.html", {"user_form": user_form})
        else:
            raise PermissionDenied


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
