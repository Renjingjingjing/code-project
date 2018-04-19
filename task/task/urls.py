from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'task.views.index'),
    url(r'^login/', include('login.urls')),
    url(r'^goods/', include('goods.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
