from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SignupView(APITestCase):

    def setUp(self):
        self.url = reverse('signup')
        return super(SignupView, self).setUp()

    def test_signup(self):
        data = {
            "email": "fane@mail.com",
            "password": "fane"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
