from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import os

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prezentacje.views.home', name='home'),
    # url(r'^prezentacje/', include('prezentacje.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^site_media/(.*)$', 'django.views.static.serve', {'document_root':os.path.join(os.path.dirname(__file__), 'site_media')}),

    url(r'^index/', 'presentations.views.index'),
    url(r'^login', 'presentations.views.login'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
