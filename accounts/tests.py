from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.


class SignUpPageTests(TestCase):
    """
    docstring
    """

    def test_signup_url_location(self):
        """
        docstring
        """
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        """
        docstring
        """
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testUser",
                "email": "testuser@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        self.assertEqual(response.status_code, 302),
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testUser")
        self.assertEqual(get_user_model().objects.all()[0].email,'testuser@email.com')
