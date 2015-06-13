from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')),
)
