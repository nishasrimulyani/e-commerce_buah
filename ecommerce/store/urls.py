from django.urls import path
from . import views
from .views import IndexView, AboutView, ShopView, CartView, create_view, shop

app_name = 'store'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('cart/', CartView.as_view(), name='cart'),
    path('create/', create_view, name='create_view'),
    path('shop/', shop, name='shop'),
    

]




