from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.


class HomePageTest(SimpleTestCase):
    """
    docstring
    """

    def test_url_exist_at_correct_location(self):
        """
        docstring
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        """
        docstring
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Home")
