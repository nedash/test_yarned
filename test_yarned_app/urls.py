from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('test_yarned_app.views',
    url(r'^$', 'person_info', name='person_info'),
    url(r'^requests/$', 'requests_info', name='requests_info'),
)
