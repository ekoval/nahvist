from django.conf.urls.defaults import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/new/$', 'nahvist.core.views.new_trip', name='new_trip'),
    url(r'^/find/$', 'nahvist.core.views.find_trip', name='find_trip'),
    url(r'^/my/$', 'nahvist.core.views.my_trips', name='my_trips'),
    url(r'^/requests/$', 'nahvist.core.views.my_requests', name='my_requests'),

    # url(r'^nahvist/', include('nahvist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
)
