from django.urls import path
from . import views
from .views import IndexView, AboutView, ContactView, ShopView

app_name = 'store'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('shop/', ShopView.as_view(), name='shop'),
]




