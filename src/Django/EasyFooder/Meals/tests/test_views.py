from django.test import TestCase
from django.contrib.auth.models import User
from Meals.models import Meal, Meal_tag, Tag, Order
from django.template import loader
import json

from datetime import datetime, timezone


class MealsApiViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user("username", "email@gmail.com", "password")

    def test_view_meals_without_auth(self):
        response = self.client.get('/meals', follow=True)
        self.assertRedirects(response, '/users/login', status_code=301)

    def test_view_orders_without_auth(self):
        response = self.client.get('/meals/orders')
        self.assertRedirects(response, '/users/login')

    def test_view_make_order_without_auth(self):
        response = self.client.get('/meals/make_order')
        self.assertRedirects(response, "/users/login")

    def test_view_meals_with_auth(self):
        self.client.login(username="username", password="password")
        response = self.client.get('/meals', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "meals.html")

    def test_view_orders_with_auth(self):
        self.client.login(username="username", password="password")
        response = self.client.get('/meals/orders')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders.html")

    def test_view_get_make_order_with_auth(self):
        self.client.login(username="username", password="password")
        response = self.client.get('/meals/make_order')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "make_order.html")

    def test_view_post_make_order_with_auth(self):
        self.client.login(username="username", password="password")
        response = self.client.get('/meals/make_order')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "make_order.html")
