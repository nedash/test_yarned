from django.conf.urls.defaults import patterns, url, include
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include("test_yarned.test_yarned_app.urls")),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^' + settings.MEDIA_URL[1:] + '(?P<path>.*)$',
	'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
)

