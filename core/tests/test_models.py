from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'foyez@email.com'
        name = 'foyez'
        password = 'testpass'

        user = get_user_model().objects.create_user(email, name, password)
        self.assertEqual(user.email, email)
        self.assertEqual(user.name, name)
        self.assertTrue(user.check_password(password))

    def test_new_user_with_email_normalized(self):
        email = 'foyez@EMAIL.COM'

        user = get_user_model().objects.create_user(
            email,
            'foyez',
            'testpass'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_without_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'foyez', 'testpass')

    # def test_new_user_with_invalid_email(self):
    #     with self.assertRaises(ValueError):
    #         get_user_model().objects.create_user('foyez@', 'foyez', 'testpass')

    def test_create_new_superuser(self):
        email = 'foyez@email.com'
        name = 'foyez'
        password = 'testpass'

        user = get_user_model().objects.create_superuser(
            email=email,
            name=name,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
