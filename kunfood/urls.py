from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()
urlpatterns = patterns('',
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^systemadmin/', include(admin.site.urls)),
#    url(r'^superadmin/', include('kunfood_admin.urls', namespace='kunfood_admin')),
    url(r'^admin/', include('client_admin.urls', namespace='client_admin')),
    url(r'^login/', 'client_admin.views.login'),
    # url(r'^add/(?P<model_name>\w+)/?$', 'tekextensions.views.add_new_model'),
    url(r'', include('app.urls')),
)
