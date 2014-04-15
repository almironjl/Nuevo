from django.conf.urls import patterns, url
from client_admin.views import *

urlpatterns = patterns('',
    # url(r'^$', rest_form, name='rest_form'),
    # url(r'local_form/$', local_form, name='local_form'),
    url(r'point_load/$', 'client_admin.views.point_load', name='point_load'),
    # url(r'product_form/$', product_form, name='product_form'),
    url(r'create_point/$', 'client_admin.views.create_point', name='create_point'),
    url(r'manage_orders/$', 'client_admin.views.manage_orders', name='manage_orders'),
    url(r'login/$', 'client_admin.views.login', name='login'),
    url(r'add_point/$', 'client_admin.views.add_point', name='add_point'),
    url(r'order_response/$', 'client_admin.views.order_response', name='order_response'),
    # url(r'popup/$', 'client_admin.views.popup', name='popup'),
    url(r'^add/(?P<model_name>\w+)/?$', 'tekextensions.views.add_new_model'),
    # url(r'add/^(?P<model_name>.+)$', 'client_admin.views.add_new_model', name='add'),
    url(r'^(?P<id>.+)$', dashboard, name='dashboard'),

)