from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defalults_to_false(self):
        item = Item.Objects.create(name='Test Todo Item')
        self.assertFalse(item.done)
