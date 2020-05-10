from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email= "test@abc.com"
        password= "Test123"
        user= get_user_model().objects.create_user(
            email= email,
            password= password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalization(self):
        email= 'test@ABCH.com'
        user= get_user_model().objects.create_user(email, 'test@123')

        self.assertEqual(user.email, email.lower())

    def test_user_create_email_normalize(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'aaa@1234')

    def test_crate_superuser(self):
        email= "test@abc.com"
        password= "Test123"
        user= get_user_model().objects.create_superuser(
            email= email,
            password= password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)