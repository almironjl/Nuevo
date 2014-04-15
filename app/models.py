# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from django.contrib.auth.models import User



#####Agregando nuestras tablas
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    admin_points = models.BooleanField(default=False, blank=True)
    admin_users = models.BooleanField(default=False, blank=True)
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.AutoField(primary_key=True)
    cel_number = models.IntegerField(max_length=15, blank=True, unique=True)
    address = models.CharField(max_length=30, blank=True)
    user = models.OneToOneField(User, related_name='superuser')
    def __str__(self):
        return self.user.username


class UserHasCompany(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User')
    representative_name = models.CharField(max_length=45, blank=True)
    ruc = models.CharField(max_length=20, blank=False, unique=True)
    firm_name = models.CharField(max_length=45, blank=False)
    commercial_name = models.CharField(max_length=45, blank=True, unique=True)
    email = models.CharField(max_length=45, blank=False, unique=True)
    phone = models.IntegerField(max_length=15, blank=False)
    address = models.CharField(max_length=30, blank=False, unique=True)
    annex = models.CharField(max_length=15, blank=False)
    web_page = models.CharField(max_length=20, blank=False)
    def __str__(self):
        return self.representative_name

class Point(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=45, blank=True, unique=True)
    city = models.CharField(max_length=45, blank=True)
    latitude = models.DecimalField(max_digits=14,blank=False, decimal_places=8)
    length = models.DecimalField(max_digits=14,blank=False, decimal_places=8)
    high = models.IntegerField(max_length=5, blank=True)
    width = models.IntegerField(max_length=5, blank=True)
    state = models.CharField(max_length=45, blank=True)
    description = models.CharField(max_length=200, blank=True)
    provider = models.CharField(max_length=20, blank=True)
    image1 = models.CharField(max_length=100, blank=True)
    image2 = models.CharField(max_length=100, blank=True)
    image3 = models.CharField(max_length=100, blank=True)
    image4 = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.address

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    des = models.CharField(max_length=45, blank=True) # I don't know it yet
    def __str__(self):
        return self.name

class TypePoint(models.Model):
    id = models.AutoField(primary_key=True)
    point = models.ForeignKey('Point')
    company = models.ForeignKey('UserHasCompany')
    type = models.ForeignKey('Type')
    price = models.IntegerField(max_length=11, blank=True)
    state = models.CharField(max_length=45, blank=True)
    def __str__(self):
        return self.company.commercial_name


class Scheduler(models.Model):
    id = models.AutoField(primary_key=True)
    type_point = models.ForeignKey('TypePoint')
    init_date = models.DateTimeField(max_length=12, blank=True)
    end_date = models.DateTimeField(max_length=12, blank=True)
    state = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return self.state

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User')
    provider = models.ForeignKey('User', related_name='user_provider')
    date = models.DateTimeField(max_length=12, blank=True)
    state = models.CharField(max_length=15, blank=True)
    def __str__(self):
        return self.name

class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    type_point = models.ForeignKey('TypePoint')
    order = models.ForeignKey('Order')
    init_date = models.DateTimeField(max_length=12, blank=True)
    end_date = models.DateTimeField(max_length=12, blank=True)
    price = models.CharField(max_length=12, blank=True)
    image = models.CharField(max_length=100, blank=True)
    movie = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name

class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    orderDetail = models.ForeignKey('OrderDetail')
    date = models.DateTimeField(max_length=12, blank=True)
    comments = models.CharField(max_length=12, blank=True)
    image = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return self.name
