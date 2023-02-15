from django.test import TestCase
from faker import Faker
from django.test import Client
from users.models import User


class PagesOpenTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/results/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        user = User.objects.create_user(username='test_user', email='tmp@tmp.ru', password='12345tmp')
        # не залогинен
        response = self.client.get('/found/')
        self.assertEqual(response.status_code, 302)
        # залогинен
        self.client.login(username='test_user', password='12345tmp')
        response = self.client.get('/found/')
        self.assertEqual(response.status_code, 200)

    def test_admin(self):
        # проверка админа
        user = User.objects.create_user(username='test_user', email='tmp@tmp.ru', password='12345tmp')
        self.client.login(username='test_user', password='12345tmp')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)
