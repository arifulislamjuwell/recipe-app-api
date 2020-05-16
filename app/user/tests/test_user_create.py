from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

USER_CREATE_URL= reverse('user:create')

def create_user(**parms):
    return get_user_model.objects.create_user(**parms)

class PublicUserApiTest(TestCase):

    def setUp(self):
        self.client= APIClient()

    def test_create_valid_user_success(self):
        payload= {
            'email':'test@gmail.com',
            'password':'test123',
            'name': 'juwel',
        }
        res= self.client.post(USER_CREATE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user= get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNoiIn('password', res.data)
    
    def test_user_already_exist(self):
        payload= {
            'email': 'test@124.com',
            'password' : 'test123'
        }
        create_user(**payload)

        res= self.client.post(USER_CREATE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        payload= {
            'email': 'test@124.com',
            'password' : 'pw'
        }
        res= self.client.post(USER_CREATE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exist= get_user_model().objects.filter(
            email= payload['email']
        ).exist()
        self.assertFalse(user_exist)