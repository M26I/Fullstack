from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):

        self.client = APIClient()
        self.menu_item = Menu.objects.create(title="Ice Cream", price=80.00, inventory=100)

    def test_get_all_items(self):

        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ice Cream")