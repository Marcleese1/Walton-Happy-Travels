# django imports
from django.conf import settings
from django.views.generic.base import View
from django.http import HttpResponseForbidden

# 3rd-party imports
import requests
from ipware import get_client_ip


def is_recaptcha_valid(request):
    """
    Verify if the response for the Google recaptcha is valid.
    """
    return requests.post(
        settings.GOOGLE_VERIFY_RECAPTCHA_URL,
        data={
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': request.POST.get('g-recaptcha-response'),
            'remoteip': get_client_ip(request)
        },
        verify=True
    ).json().get("success", False)



def human_required(view_func):
    """
    This decorator is aimed to verify Google recaptcha in the backend side.
    """
    def wrapped(request, *args, **kwargs):
        if is_recaptcha_valid(request):
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return wrapped