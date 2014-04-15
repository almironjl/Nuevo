from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'app.views.home', name='home'),
    # url(r'^signup-email/', 'app.views.signup_email'),
    # url(r'^email-sent/', 'app.views.validation_sent'),
        # url(r'^login/$', 'app.views.home'),
    url(r'^logout/$', 'app.views.logout', name='logout'),
    url(r'^done/$', 'app.views.done', name='done'),
    # url(r'^email/$', 'app.views.require_email', name='require_email'),
    #
    #
    # #url(r'^getvideourl_servicio/(?P<valor>.+)$', 'app.views.getvideourl_servicio', name='getvideourl_servicio'),
    # #
    url(r'^busqueda/$', 'app.views.busqueda', name='busqueda'),
    url(r'^company_details/(?P<id>.+)$', 'app.views.company_details', name='company_details'),
    # #url(r'^obten_busqueda/$', 'app.views.obten_busqueda', name='busqueda'),
    # #url(r'^obten_busqueda_servicio/$', 'app.views.obten_busqueda_servicio', name='busqueda'),
    # #
    url(r'^search_restaurants/$', 'app.views.search_restaurants', name='search_restaurants'),
    url(r'^search_points/$', 'app.views.search_points', name='search_points'),
    url(r'^search_companies/$', 'app.views.search_companies', name='search_companies'),
    url(r'^orders_view/$', 'app.views.orders_view', name='orders_view'),
    # url(r'^get_products/$', 'app.views.get_products', name='get_products'),
    # url(r'^search_simproduct_restaurants/$', 'app.views.search_simproduct_restaurants', name='search_simproduct_restaurants'),
    # #
    # #url(r'^obten_tags/(?P<tag>.+)$', 'app.views.obten_tags', name='obten_tags'),
    # #url(r'^register/$', 'app.views.register_form', name='register'),
    # #url(r'^restaurant_confirmacion/(?P<token>.+)$', 'app.views.restaurant_confirmacion', name='restaurant_confirmacion'),
    url(r'^detail/(?P<id>.+)$', 'app.views.detail', name='detail'),
    #
    url(r'^experiencia/$', 'app.views.experiencia', name='experiencia'),
    # #url(r'^restaurant_delivery/$', 'app.views.restaurant_delivery', name='restaurant_delivery'),
    url(r'^buyings/$', 'app.views.buyings', name='buyings'),
    url(r'^delete_order/$', 'app.views.delete_order', name='delete_order'),
    url(r'^order_service/$', 'app.views.order_service', name='order_service'),
    url(r'^guia/$', 'app.views.guia', name='guia'),
    url(r'^ayuda/$', 'app.views.ayuda', name='ayuda'),
    url(r'^addto_car/(?P<id>.+)$', 'app.views.addto_car', name='addto_car'),
    url(r'^check_availability/(?P<id>.+)$', 'app.views.check_availability', name='check_availability'),
    # url(r'^restaurant_update_status/(?P<restaurant_id>.+)/(?P<restaurant_status>.+)$', 'app.views.restaurant_update_status', name='restaurant_update_status'),
    # url(r'^save_list/', 'app.views.save_list', name='save_list'),
    # url(r'^restaurant_delivery_service/', 'app.views.restaurant_delivery_service', name='restaurant_delivery_service')
)
