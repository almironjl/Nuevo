from django.forms import ModelForm
from app.models import OrderDetail, Order


class OrderDetailForm (ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['order', 'init_date', 'end_date', 'price' , 'image', 'movie']
