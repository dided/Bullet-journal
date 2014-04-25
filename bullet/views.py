from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail


class RegistrationViewUniqueEmail(RegistrationView):
    form_class = RegistrationFormUniqueEmail

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


    
