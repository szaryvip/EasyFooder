from django.test import TestCase
from django.contrib.auth.models import User
from django.template import loader
import json

from datetime import datetime, timezone


class UsersApiViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user("username", "email@gmail.com", "password")

    def test_view_index_without_auth(self):
        response = self.client.get('/')
        self.assertRedirects(response, "/users/login")

    def test_view_index_with_auth(self):
        self.client.login(username="username", password="password")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_view_login_without_auth(self):
        response = self.client.get('/users/login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_view_register_without_auth(self):
        response = self.client.get('/users/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register.html")
