from django.conf.urls.defaults import *
from test_yarned_app import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^$', views.userInfo),
)

