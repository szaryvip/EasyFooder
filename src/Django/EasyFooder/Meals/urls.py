from django.urls import path

from . import views

urlpatterns = [
    path('orders', views.orders, name='orders'),
    path('make_order', views.make_order, name='make_order')
]
