from django.conf.urls import patterns, url
from django.contrib.auth.forms import *


from programming_templates import views

urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'programming_templates/login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'programming_templates/login.html'}),
    url(r'^$', views.dashboard, name='dashboard')
)
