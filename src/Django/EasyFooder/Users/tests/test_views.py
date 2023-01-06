from django.test import TestCase
from django.contrib.auth.models import User
from django.template import loader
import json

from datetime import datetime, timezone


class UsersApiViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user("username", "email@gmail.com", "password")

    def test_view_get_index_without_auth(self):
        response = self.client.get('/')
        self.assertRedirects(response, "/users/login")

    def test_view_get_index_with_auth(self):
        self.client.login(username="username", password="password")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_view_get_login_without_auth(self):
        response = self.client.get('/users/login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_view_get_register_without_auth(self):
        response = self.client.get('/users/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register.html")

    def test_view_post_login(self):
        response = self.client.post('/users/login',
                                    json.dumps({'username': 'username',
                                                'password': 'password'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_view_post_register(self):
        response = self.client.post('/users/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register.html")

    def test_view_get_logout(self):
        response = self.client.get("/users/logout")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/users/login")
