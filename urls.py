from django.conf.urls.defaults import patterns, url, include
from django.conf import settings
from django.contrib.auth.views import login, logout
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include("test_yarned.test_yarned_app.urls")),
    url(r'^accounts/login/$', login, {'template_name': 'login.html'}, name='auth_login'),
    url(r'^accounts/logout/$', logout,  {'next_page': '/'}, name='auth_logout'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^' + settings.MEDIA_URL[1:] + '(?P<path>.*)$',
	'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
)

