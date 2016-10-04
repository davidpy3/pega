from django.conf.urls import patterns, include, url
from django.contrib import admin

from pegasus.apps.humanresources.views import DashboardView


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^rrhh/', include('pegasus.apps.humanresources.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
