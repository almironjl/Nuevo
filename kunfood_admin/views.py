import json
import os
import string
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string
from app.models import Type_Point, Point, Type,  User, UserHasCompany


def dashboard(request):
    restaurant_request = RestaurantRequest.objects.all()
    context = {
        'restaurant_request': restaurant_request
    }
    return render(request, 'kunfood_admin/dashboard.html', context)

# approve a restaurant request for stay in kf
def confirm_register(request):
    id = request.POST.get('id')
    restaurant_request = RestaurantRequest.objects.get(pk=int(id))
    if restaurant_request.status == RestaurantRequest.FOR_ADMIN_CONFIRM:
        restaurant_request.status = RestaurantRequest.FOR_COMPLETE_INFO
        restaurant_request.save()

        restaurant = Restaurant()
        restaurant.name = restaurant_request.restaurant_name
        restaurant.email = restaurant_request.email
        restaurant.address = restaurant_request.address
        restaurant.restaurant_request = restaurant_request
        restaurant.save()

        user = User()
        user.name = restaurant_request.name
        user.email = restaurant_request.email
        user.password = generate_random_string(length=10, stringset=string.ascii_letters)
        user.save()

        restaurant_has_user = RestaurantHasUser()
        restaurant_has_user.user = user
        restaurant_has_user.restaurant = restaurant
        restaurant_has_user.profile = Profile.objects.get(pk=Profile.REST_ADMIN)
        restaurant_has_user.save()

        subject = "CONFIRMACION: REGISTRO NUEVO RESTAURANTE : KUNFOOD"
        message = render_to_string('kunfood_admin/mail/account_data.html',
                                   {'user': user.email,
                                    'password': user.password,
                                    'host': str(request.get_host()),
                                    'service':'/admin'
                                   })
        email = EmailMessage(subject, message, to=['bichocj@gmail.com'])
        email.content_subtype = "html"
        email.send()

    result = {
        'display': restaurant_request.get_status_display(),
        'status': restaurant_request.status,
    }
    return HttpResponse(json.dumps(result), content_type="application/json")


def generate_random_string(length, stringset=string.ascii_letters + string.digits + string.punctuation):
    return ''.join([stringset[i % len(stringset)] \
                    for i in [ord(x) for x in os.urandom(length)]])
