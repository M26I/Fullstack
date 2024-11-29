from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice Cream", price=80.00, inventory=100)
        self.assertEqual(str(item), "Ice Cream : 80.00")