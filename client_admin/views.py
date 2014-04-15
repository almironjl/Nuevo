from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import user_logged_in, login as auth_login, authenticate
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.utils.html import escape
from django.forms.models import modelform_factory
from django.db.models.loading import get_models, get_app, get_apps
from app.models import User, Order, OrderDetail, TypePoint, Point, Type, UserHasCompany
from django.contrib.auth.models import User as auth_User
from client_admin import forms
from client_admin.forms import PointForm


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # user = auth_User.objects.get(email=email, password= password)
        auth_user = authenticate(username = password, password= password)
        # user_object = User.objects.filter(user__email=email, user__username=password)
        if auth_user:
            request.session['user'] = email
            auth_login(request, auth_user)
            if request.GET.get('next', False):
                return HttpResponseRedirect(request.GET.get('next'))
            else:
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

@login_required
def dashboard(request, id):
    user = User.objects.get(user= request.user)
    order_objects = Order.objects.all()
    mlist = list()
    for m in order_objects:
        if user.id == m.provider.id:
            detail = OrderDetail.objects.get(pk=m.id)
            mlist.append({'point':detail.type_point.point.address, 'state':m.state})
    size = mlist.__len__()
    context = {
        'user': user,
        'orders': mlist,
        'size':size
    }
    return render(request, 'dashboard.html', context)

@login_required
def manage_orders(request):
    user = User.objects.get(user__id=request.user.id)
    order_objects = OrderDetail.objects.filter(order__provider__user=user)
    context = {
        'orders': order_objects
    }
    return render(request, 'manage_orders.html', context)

@login_required
def order_response(request):
    user = User.objects.get(user__id=id)
    user = User.objects.get(user__id=request.user.id)
    order_objects = OrderDetail.objects.filter(order__provider__user=user)
    context = {
        'orders': order_objects
    }
    return render(request, 'manage_orders.html', context)

@login_required
def create_point(request):
    user = User.objects.get(user__id=request.user.id)
    typepoints_objects = TypePoint.objects.filter(company__user__user=user)
    orders = list()
    for m in typepoints_objects:
        if not orders.__contains__('m.address'):
            temp_objects = OrderDetail.objects.filter(order__provider=user,type_point__point=m.point)
            # if temp_objects.__len__() != 0:
            orders.append({'id':m.point.id,'image':m.point.description,'type': m.type.name, 'address':m.point.address,'num_orders':temp_objects.__len__()})

    context = {
        'points': typepoints_objects,
        'orders': orders
    }
    return render(request, 'create_point.html', context)

@login_required
def add_point(request):
    user = User.objects.get(user__id=request.user.id)
    points_objects = Point.objects.all()
    types_objects = Type.objects.all()
    companies_objects = UserHasCompany.objects.filter(user = user)
    context = {
        'points': points_objects,
        'companies': companies_objects,
        'types':types_objects
    }
    return render(request, 'add_point.html', context)

#
# def rest_form(request):
#     if request.method == 'POST':
#         form = RestaurantForm(request.POST or None)
#         if form.is_valid():
#             pass
#     else:
#         restaurant = Restaurant.objects.get(pk=1)
#         form = RestaurantForm(instance=restaurant)
#
#     context = {
#         'form': form,
#         'restaurant': restaurant,
#     }
#
#     return render(request, 'client_admin/rest_form.html', context)
#
#
# def local_form(request):
#     restaurant = Restaurant.objects.get(pk=1)
#     if request.method == 'POST':
#         pk = request.POST.get('id')
#         if pk:
#             form = LocalForm(request.POST, instance=Local.objects.get(pk=pk))
#         else:
#             form = LocalForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#     else:
#         form = LocalForm()
#
#     locals = Local.objects.filter(restaurant=restaurant)
#
#     #districts = District.objects.all();
#
#     context = {
#         'form': form,
#         'locals': locals,
#         'restaurant': restaurant,
#         'is_new': True,
#     }
#     return render(request, 'client_admin/form_local.html', context)
#
#
@login_required
def popup(request):
    return render(request, 'popup.html')

@login_required
def point_load(request):
    if request.method != 'POST':
        return redirect('client_admin:create_point')
    id = request.POST.get('id')
    point = Point.objects.filter(id=id)
    form = TypePoint.objects.filter(company__user__user=request.user, point=point)#Manejar session
    context = {
        'points':form,
        'orders':form
    }
    return render(request, 'create_point.html', context)

    # local = Local.objects.get(pk=id)
    # form = LocalForm(instance=local)
    #
    # locals = Local.objects.filter(restaurant=restaurant)

    # context = {
    #     # 'form': form,
    #     # 'locals': locals,
    #     # 'restaurant': restaurant,
    # }
    #
    # return render(request, 'create_point.html', context)

#
# def product_form(request):
#     categories = Category.objects.all()
#     restaurant = Restaurant.objects.get(pk=1)
#     if request.method == 'POST':
#         form = ProductForm(request.POST or None)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.restaurant = restaurant
#             product.save()
#     else:
#         form = ProductForm()
#
#     context = {
#         'form': form,
#         'categories': categories,
#         'products': Product.objects.all
#     }
#     return render(request, 'client_admin/form_product.html', context)
#
#
# context_processors.py
from django.conf import settings

def admin_media_prefix(request):
    return {'ADMIN_MEDIA_PREFIX': settings.ADMIN_MEDIA_PREFIX }

@login_required
def add_new_model(request, model_name):
    if (model_name.lower() == model_name):
        normal_model_name = model_name.capitalize()
    else:
        normal_model_name = model_name

    app_list = get_apps()
    for app in app_list:
        for model in get_models(app):
            if model.__name__ == normal_model_name:
                form = modelform_factory(model)

                if request.method == 'POST':
                    form = form(request.POST)
                    if form.is_valid():
                        try:
                            new_obj = form.save()
                        except forms.ValidationError, error:
                            new_obj = None

                        if new_obj:
                            return HttpResponse('<script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");</script>' % \
                                (escape(new_obj._get_pk_val()), escape(new_obj)))

                else:
                    form = form()

                page_context = {'form': form, 'field': normal_model_name}
                return render_to_response('popup.html', page_context, context_instance=RequestContext(request))