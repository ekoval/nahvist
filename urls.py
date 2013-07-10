from django.conf.urls.defaults import patterns, include, url
from core.forms import UserRegistrationForm
from registration.backends.default.views import RegistrationView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'nahvist.core.views.about_project', name='home'),
    url(r'^trip', include('core.urls')),
    # url(r'^nahvist/', include('nahvist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=UserRegistrationForm), name='registration_register'),
    url(r'^accounts/', include('registration.urls')),
)

