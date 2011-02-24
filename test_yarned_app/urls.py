from django.conf.urls.defaults import *

urlpatterns = patterns('test_yarned_app.views',
    url(r'^$', 'personInfo', name = 'person_info'),
    url(r'^requests/$', 'requestsInfo', name = 'requests_info'),
)
