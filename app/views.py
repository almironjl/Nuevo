import json
import os
import string
import datetime
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.db import connection
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.template.loader import render_to_string

from social.backends.google import GooglePlusAuth

from app.forms import OrderDetailForm
from app.models import Order, OrderDetail, Point, User, UserHasCompany, Type, TypePoint, Scheduler, Contract

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return render_to_response('home.html', {}, RequestContext(request))


def home(request):
    type_objects = Type.objects.all()
    if request.user.is_authenticated():
        return redirect('done')
    return render_to_response('home.html', {
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'type_objects': type_objects,
    }, RequestContext(request))

@login_required
def done(request):
    type_objects = Type.objects.all()
    scope = ' '.join(GooglePlusAuth.DEFAULT_SCOPE)
    return render_to_response('home.html', {
        """Login complete view, displays user data"""
        'user': request.user,
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': scope,
        'type_objects': type_objects,
        }, RequestContext(request))

#
# def signup_email(request):
#     return render_to_response('email_signup.html', {}, RequestContext(request))
#
#
# def validation_sent(request):
#     return render_to_response('validation_sent.html', {
#         'email': request.session.get('email_validation_address')
#     }, RequestContext(request))
#
#
# def require_email(request):
#     if request.method == 'POST':
#         request.session['saved_email'] = request.POST.get('email')
#         backend = request.session['partial_pipeline']['backend']
#         return redirect('social:complete', backend=backend)
#     return render_to_response('email.html', RequestContext(request))
#
# ######################################################################
#
def busqueda(request):
    type_objects = Type.objects.all()
    type = request.POST.get('type')
    city = request.POST.get('city')
    context = {
        'type_objects': type_objects,
        'type': type,
        'city': city, # 'rests': restaurant_objects,
    }
    return render(request, 'busqueda.html', context)

@login_required
def addto_car(request, id):
    if request.method == 'POST':
        contract_objects = Contract.objects.filter(orderDetail__type_point_id = id)
        last_date = datetime.datetime.today()
        for m in contract_objects:
            if m.orderDetail.end_date > last_date:
                last_date = m.orderDetail.end_date
        numbofMonths = int(request.POST.get('months'))
        init_date = last_date
        end_date = init_date + datetime.timedelta(days =  numbofMonths*30)
        type_point_object = TypePoint.objects.get(pk=id)
        user = User.objects.get(user = request.user)
        order_object = Order(user_id=user.id, provider_id = type_point_object.company.user.id, date = datetime.date.today(), state = 'espera')
        order_object.save()
        orderDetail_object = OrderDetail(
            type_point_id = type_point_object.id,
            order_id = order_object.id,
            init_date = init_date,
            end_date = end_date,
            price = type_point_object.price*numbofMonths,
            image = 'images/example',
            movie = 'movies/example'
        )
        orderDetail_object.save()
        orders_object = OrderDetail.objects.filter(order__user=user, order__state= "pendiente")
        context = {
            'point_type': id,
            'my_orders': orders_object,
            'order_object' : order_object
        }
        return render(request, 'check_availability.html', context)
    else:
        context = {
            'point_type': id
        }
        return render(request, 'check_availability.html', context)

@login_required
def buyings(request):
    if request.method == 'POST':
        id = request.POST.get('row')
        order_object = OrderDetail.objects.get(pk=id)
        orderID = order_object.order.id
        OrderDetail.objects.filter(order__id=orderID).delete()
        Order.objects.filter(id=orderID).delete()
    # user = User.objects.get(user = id)
    user = User.objects.get(user = request.user)
    orders_object = OrderDetail.objects.filter(order__user=user)
    context = {
        'my_orders': orders_object
    }
    return render(request, 'buyings.html', context)

@login_required
def delete_order(request):
    # user = User.objects.get(user = id)
    id = request.POST.get('row')
    order_object = OrderDetail.objects.get(pk=id)
    orderID = order_object.order.id
    OrderDetail.objects.filter(order__id=orderID).delete()
    Order.objects.filter(id=orderID).delete()
    user = User.objects.get(user = request.user)
    orders_object = OrderDetail.objects.filter(order__user=user)
    context = {
        'my_orders': orders_object
    }
    return render(request, 'buyings.html', context)

@login_required
def order_service(request):
    user = request.user
    if request.method == 'POST':
        orders_object = OrderDetail.objects.filter(order__user=user)
        for m in order_service:
            if m.state == 'ESPERA':

        return render(request, 'orders_view.html', context)
    else:
        return render(request, 'order_service.html', context)

# def seacrh_restaurants(request):
#     food = request.POST.get('food')
#     place = request.POST.get('place')
#     page = request.POST.get('page')
#
#     restaurant = Restaurant()
#     page = int(page) - 1
#     sql = restaurant.obten_busqueda(platoTag=food, lugar=place, offset=page, limit=10)
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     restaurant_objects = dictfetchall(cursor)
#     context = {
#         'titulo': 'Kunfood - vive la Experiencia',
#         'key': food,
#         'lugar': place,
#         'pagina': page,
#         'restaurants': restaurant_objects
#     }
#     return HttpResponse(json.dumps(restaurant_objects), content_type="application/json")
#
#
# def register_form(request):
#     if request.method == 'POST':
#         form = RestaurantRequestForm(request.POST or None)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             register = RestaurantRequest.objects.filter(email=email)
#             if register.count() > 0:
#                 #registro existente
#                 context = {
#                     'request': request
#                 }
#                 #return render(request, 'register_form.html', context)
#                 return HttpResponse(123)
#             restaurant_request = form.save(commit=False)
#             restaurant_request.confirmation_token = generate_random_string(length=10)
#             restaurant_request.save()
#             subject = "REGISTRO NUEVO RESTAURANTE : KUNFOOD"
#             message = render_to_string('mail/register_verification.html',
#                                        {"name": restaurant_request.name, "address": restaurant_request.address,
#                                         'phone': restaurant_request.phone,
#                                         'email': restaurant_request.email,
#                                         'website': restaurant_request.website,
#                                         'host': str(request.get_host()),
#                                         'confirmation_token':restaurant_request.confirmation_token
#                                        })
#             email = EmailMessage(subject, message, to=['bichocj@gmail.com'])
#             email.content_subtype = "html"
#             email.send()
#             context = {
#                 'title': 'Registro satisfactorio',
#                 'description': 'le ha sido enviado un correo para verificar sus datos',
#             }
#             return render(request, 'message.html', context)
#     else:
#         form = RestaurantRequestForm()
#
#
#     context = {
#         'form': form
#     }
#     return render(request, 'register_form.html', {'form': form})
#
# def register_confirmation(request, token):
#     try:
#         restaurant_request = RestaurantRequest.objects.get(confirmation_token=token, status=RestaurantRequest.FOR_EMAIL_CONFIRM)
#         restaurant_request.status = RestaurantRequest.FOR_ADMIN_CONFIRM
#         restaurant_request.save()
#         message = "Su registro ha sido actualizado, el administrador de kunfood validara tu informacion"
#     except RestaurantRequest.DoesNotExist:
#         message = "No se ha encontrado su token"
#     except RestaurantRequest.MultipleObjectsReturned:
#         message = "Registro duplicado"
#     context = {
#         'title': 'Confirmacion',
#         'description': message,
#     }
#     return render(request, 'message.html', context)
#
def search_points(request):
    points_objects = Point.objects.all()
    city = request.POST.get('city')
    mlist = list()
    for m in points_objects:
        if m.city == city:
            mlist.append({'point':m.id,'address':m.address,'city':m.city,'width':m.width,'lat':m.latitude,'lng':m.length,})

    return HttpResponse(json.dumps(mlist), content_type="application/json")

def search_companies(request):
    typepoints_objects = TypePoint.objects.all()
    companies_objects = UserHasCompany.objects.all()
    point = request.POST.get('point')
    mlist = list()
    for m in typepoints_objects:
        if m.point.id.__str__() == point:
            mlist.append({'id':m.id,'name':m.company.commercial_name,'type':m.type.name})

    return HttpResponse(json.dumps(mlist), content_type="application/json")


def search_restaurants(request):
    user = '%' + request.POST.get('type') + '%'
    commercial_name = '%' + request.POST.get('city') + '%'
    page = request.POST.get('page')
    company_objects = UserHasCompany.objects.raw('''
        select
        app_userhascompany.*
        FROM
        `app_userhascompany`
        GROUP BY
        `app_userhascompany`.id
    ''', tuple([user, commercial_name]))
    mlist = list()
    for m in company_objects:
        mlist.append({'id': m.id,'address': m.address, 'phone': m.phone, 'representative': m.representative,'price':m.price})

    return HttpResponse(json.dumps(mlist), content_type="application/json")

# Where product.name like %s And local.address like %s
# Inner Join local_has_product ON `local`.id = local_has_product.local_id
#         Inner Join product ON local_has_product.product_id = product.id
#         Inner Join restaurant ON restaurant.id = `local`.restaurant_id

#
#     food = '%' + request.POST.get('food') + '%'
#     place = '%' + request.POST.get('place') + '%'
#     page = request.POST.get('page')
#     restaurant_objects = Local.objects.raw('''
#         select
#         local.*
#         FROM
#         `local`
#         Inner Join local_has_product ON `local`.id = local_has_product.local_id
#         Inner Join product ON local_has_product.product_id = product.id
#         Inner Join restaurant ON restaurant.id = `local`.restaurant_id
#         Where product.name like %s And local.address like %s
#         GROUP BY
#         `local`.id
#     ''', tuple([food, place]))
#
#     mlist = list()
#     for m in restaurant_objects:
#         mlist.append({'id': m.id,'name': m.name,'address': m.address, 'phone': m.phone, 'imageurl': m.imageurl, 'lat':m.lat,'lng':m.lng,})
#
#     return HttpResponse(json.dumps(mlist), content_type="application/json")
#
# def search_simproduct_restaurants(request):
#     localid = request.POST.get('localid')
#
#     restaurant_objects = Local.objects.raw('''
#         SELECT
#         `local`.*
#         FROM
#         `local`
#         INNER JOIN product ON product.restaurant_id = `local`.restaurant_id
#         INNER JOIN (
#             SELECT
#             product.id AS restproduct
#             FROM
#             product
#             INNER JOIN local_has_product ON local_has_product.product_id = product.id
#             WHERE local_has_product.local_id = %s
#         ) AS T
#         WHERE product.id = T.restproduct AND `local`.id != %s
#         GROUP BY
#         `local`.id
#     ''', tuple([localid, localid]))
#
#     mlist = list()
#     for m in restaurant_objects:
#         mlist.append({'id': m.id,'name': m.name,'address': m.address, 'phone': m.phone, 'imageurl': m.imageurl, 'lat':m.lat,'lng':m.lng,})
#     return HttpResponse(json.dumps(mlist), content_type="application/json")
#
#
#
# def get_products(request):
#     localid = request.POST.get('localid')
#
#     product_objects = Product.objects.raw('''
#         SELECT
#         product.*,
#         local_has_product.price
#         FROM
#         product
#         INNER JOIN local_has_product ON local_has_product.product_id = product.id
#         WHERE local_has_product.local_id = %s
#     ''', localid)
#
#     mlist = list()
#     for m in product_objects:
#         mlist.append({'name': m.name, 'price': m.price, 'imageurl': m.imageurl})
#
#     return HttpResponse(json.dumps(mlist), content_type="application/json")
#

def detail(request, id):
    point = Point.objects.get(id=id)
    context = {
        'point': point
    }
    return render(request, 'detail.html', context)

def orders_view(request):
    user = User.objects.get(user = request.user)
    orders_objects = OrderDetail.objects.filter(order__user=user)
    context = {
        'my_orders' : orders_objects
    }
    return render(request, 'orders_view.html', context)

def experiencia(request):
    context = {
        'title': "titulo"
    }
    return render(request, 'experiencia.html', context)
#
#
# def restaurant_delivery(request):
#     local_id = request.GET['local_id']
#
#     local = Local.objects.get(id=local_id)
#     restaurant = local.restaurant
#     local_has_products = LocalHasProduct.objects.filter(local = local_id)
#     categories = set()
#
#     for local_has_product in local_has_products:
#         product_id = local_has_product.product_id
#         product = Product.objects.get(id = product_id)
#         categories.add(product.category)
#
#     context = {
#         'local': local,
#         'restaurant': restaurant,
#         'local_categories': categories
#     }
#
#     return render(request, 'restaurant_delivery.html', context)
#
#
# def restaurant_delivery_service(request):
#     local_id = int(request.POST['local_id'])
#     category_id = int(request.POST['category_id'])
#
#     local_has_products = LocalHasProduct.objects.filter(local = local_id)
#     menu = []
#
#     for local_has_product in local_has_products:
#         product = Product.objects.get(id = local_has_product.product_id)
#
#         if product.category.id == category_id:
#             data = {
#                 'id': product.id,
#                 'name': product.name,
#                 'price': local_has_product.price
#             }
#             menu.append(data)
#
#     return HttpResponse(json.dumps(menu), content_type="application/json")
#
def ayuda(request):
    context = {
    }
    return render(request, 'ayuda.html', context)
#
def guia(request):
    context = {
    }
    return render(request, 'guia.html', context)

def company_details(request, id):
    features = TypePoint.objects.get(id=id)
    company = UserHasCompany.objects.get(id=features.company.id)
    context ={
        'features':features,
        'company':company
        # 'id':id,
        # 'address':address,
        # 'phone':phone,
        # 'representative':representative,
        # 'price':price,
    }
    return render(request, 'company.html', context)

def check_availability(request, id):
    scheduler_objects = Scheduler.objects.all()
    scheduler = list()
    for m in scheduler_objects:
        if m.type_point.id.__str__() == id:
            scheduler.append({'init_date':m.init_date,'end_date':m.end_date,'state':m.state,})
    context ={
        'scheduler':scheduler,
        'point_type':id
    }
    return render(request, 'check_availability.html', context)


# def ws(request):
#     post = request.POST
#     post_getlist = request.POST.getlist('platos[]')
#     # data=request.POST.getlist['platos[]']
#
#     for key in request.POST.iterkeys():
#         valuelist = request.POST.getlist(key)
#         i = 0
#     return HttpResponse(1)
#
#
# def dictfetchall(cursor):
#     "Returns all rows from a cursor as a dict"
#     desc = cursor.description
#     return [
#         dict(zip([col[0] for col in desc], row))
#         for row in cursor.fetchall()
#     ]
#
#
# def generate_random_string(length, stringset=string.ascii_letters + string.digits + string.punctuation):
#     return ''.join([stringset[i % len(stringset)] \
#                     for i in [ord(x) for x in os.urandom(length)]])


# def getvideourl_servicio(request, valor):
#     out = ""
#     if valor == '1':
#         out += '<iframe width="100%" height="400px" src="http://player.vimeo.com/video/73319422" frameborder="0" allowfullscreen></iframe>'
#     elif valor == '2':
#         out += '<iframe width="100%" height="400px"src="http://player.vimeo.com/video/73320474" frameborder="0" allowfullscreen></iframe>'
#     elif valor == '3':
#         out += '<iframe width="100%" height="400px" src="http://player.vimeo.com/video/73320388" frameborder="0" allowfullscreen></iframe>'
#     elif valor == '4':
#         out += '<iframe width="100%" height="400px" src="http://player.vimeo.com/video/73320550" frameborder="0" allowfullscreen></iframe>'
#
#     # results = [ob.as_json() for ob in rest]
#     # results = []
#     return HttpResponse(out)
#     # return HttpResponse()


# def save_list(request):
#     form = RestaurantDeliveryForm(request.POST or None)
#     return HttpResponse("1")
#
