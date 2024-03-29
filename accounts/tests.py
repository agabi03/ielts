from django.test import TestCase
from django.urls import reverse
from .models import CustomUser


class UserRegistrationTestCase(TestCase):
    def test_user_registration(self):
        data = {'username': 'testuser', 'password1': 'dfgjndfgjndfgjn', 'password2': 'dfgjndfgjndfgjn'}
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 302)  # Перенаправление после успешной регистрации
        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())
