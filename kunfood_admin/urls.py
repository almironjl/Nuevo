from django.conf.urls import patterns, url
from kunfood_admin.views import *

urlpatterns = patterns('',
    url(r'^$', dashboard, name='dashboard'),
    url(r'^/confirm_register$', confirm_register, name='confirm_register'),
)