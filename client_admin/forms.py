from django import forms
from django.db.models import Model
from django.forms import ModelForm
# from app.models import RestaurantRequest, Restaurant, Local, Product, Category
from app.models import Point
from tekextensions.widgets import SelectWithPopUp

class CustomForm(forms.Form):
    points = forms.ModelChoiceField(Point.objects, widget=SelectWithPopUp)
# class RestaurantForm(ModelForm):
#     class Meta:
#         model = Restaurant
#         fields = ['email', 'name', 'phone', 'address', 'website', ]
#
#
# class LocalForm(ModelForm):
#     class Meta:
#         model = Local
#         fields = ['id', 'name', 'phone', 'address', 'city', 'district', 'street', 'restaurant']
#
#
# class ProductForm(ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'category', ]
class PointForm(ModelForm):
    class Meta:
        model = Point
        fields = ['id', 'address', 'city', 'latitude', 'length', 'high', 'width', 'state','description','provider']


# class CustomForm(forms.Form):
#     selectfield = forms.ModelChoiceField(Model.objects, widget=SelectWithPopUp)