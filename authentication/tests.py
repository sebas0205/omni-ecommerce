from django.contrib.auth import get_user_model
from django.test import TestCase


# Create your tests here.
class ModelTest(TestCase):

    def test_user_email_creation(self):
        """Test new user creation"""
        email = "user@email.com"
        password = 'Testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)

    def test_user_bad_email(self):
        """Test for creating an user not email set"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'TestPassword')


