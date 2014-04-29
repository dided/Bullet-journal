from django.conf.urls import patterns, include, url

from django.contrib import admin
from .views import RegistrationViewUniqueEmail

from django.contrib.auth.views import login
from django.contrib.auth.decorators import user_passes_test
admin.autodiscover()

login_forbidden = user_passes_test(lambda u: u.is_anonymous(), '/app/')

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bullet.views.index', name='index'),
    url(r'^api/', include('api.urls')),
    url(r'^app', 'bullet.views.start_app', name='app'),
    url(r'^register/$', RegistrationViewUniqueEmail.as_view(), name='registration_register'),
    url(r'^login/', login_forbidden(login), name='user_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)
