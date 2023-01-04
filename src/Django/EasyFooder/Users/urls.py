from django.urls import path

from . import views

urlpatterns = [
    path('orders', views.orders, name='orders'),
    path('make_order', views.make_order, name='make_order'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('', views.index, name="index")
]
