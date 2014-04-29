from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from registration.backends.simple.views import RegistrationView 
from registration.forms import RegistrationFormUniqueEmail
from registration.signals import user_registered

from api.models import Page


class RegistrationViewUniqueEmail(RegistrationView):
    form_class = RegistrationFormUniqueEmail
    def get_success_url(self, request, user):
        return '/app/'
    

def create_index_page(sender, user, request, **kwargs):
    page = Page.objects.create(title='Index', page_number=1, user=user)


def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', {}, context)


@login_required
def start_app(request):
    context = RequestContext(request)
    return render_to_response('app.html', {}, context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('index')


# When user is registered, create index page for him
user_registered.connect(create_index_page)
