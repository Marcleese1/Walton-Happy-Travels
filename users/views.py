# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import UserCustomerForm, UserChangeForm, CustomerChangeFormAdmin
from .models import Customer


class SignUp(generic.CreateView):
    form_class = UserCustomerForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def delete_user(request, email):
    context = {}

    try:
        u = Customer.objects.get(email = email)
        u. delete()
        context['msg'] = 'The User is Deleted'
    except Customer.DoesNotExist:
        context['msg'] = 'User does not exist.'
    except Exception as e:
        context['msg'] = e.message

    return render(request, 'home.html', context=context)
