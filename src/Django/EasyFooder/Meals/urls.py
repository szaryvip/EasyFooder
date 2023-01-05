from django.urls import path

from . import views

urlpatterns = [
    path('meals/orders', views.orders, name='orders'),
    path('meals/make_order', views.make_order, name='make_order'),
    path('meals/', views.meals, name='meals')
]
