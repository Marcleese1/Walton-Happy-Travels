from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView
from users.models import Customer
from users.views import CustomerChangeFormAdmin
from django.shortcuts import render, redirect
from .forms import BookingForm
from.models import Bookings
from django.http import Http404


class BookingViewMixin(object):
    model = Bookings
    form_class = BookingForm


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


class BookingDetailView(BookingViewMixin, DetailView):
    def dispatch(self, request, *args, **kwargs):
        self.kwargs = kwargs
        self.object = self.get_object()
        if request.user.is_authenticated():

            if not self.object.user == request.user:
                raise Http404
            else:
                session = self.object.session
                if(not session or not request.session.session_key or session.session_key !=
                        request.session.session_key):
                    raise Http404
            return super(BookingViewMixin,self).dispatch(request, *args, **kwargs)


class BookingListView(BookingViewMixin, ListView):
    """View to display all ``Booking`` instances of one user."""
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BookingViewMixin, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.bookings.all()
