from django.conf.urls import patterns, include, url

urlpatterns = patterns('goods.views',
    url(r'^default', 'default'),
    url(r'^picture/(\d+)', 'picture'),
    url(r'^upload', 'upload'),
    url(r'^post', 'post'),
    url(r'^preview', 'preview'),
    url(r'^work', 'work'),
    url(r'^study', 'study'),
    url(r'^search', 'search'),
)
