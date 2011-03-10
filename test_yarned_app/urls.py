from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('test_yarned_app.views',
    url(r'^$', 'person_info', name='person_info'),
    url(r'^requests/$', 'requests_info', name='requests_info'),
    url(r'^person_info_edit/$', 'person_info_edit', name='person_info_edit'),
    url(r'^operation_log/$', 'operation_log', name='operation_log'),
)
