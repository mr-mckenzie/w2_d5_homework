import unittest
from classes.guest import Guest

class TestGuest (unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Alice", 50)

    def test_guest_has_name(self):
        self.assertEqual("Alice", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(50, self.guest.wallet)

    def test_guest_pays_money(self):
        self.guest.pay_money(15)
        self.assertEqual(35, self.guest.wallet)
