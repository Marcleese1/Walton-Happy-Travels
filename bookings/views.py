from django.views.generic import TemplateView
from users.models import Customer


class HomePageView(TemplateView):
    model = Customer
    template_name = 'home.html'

