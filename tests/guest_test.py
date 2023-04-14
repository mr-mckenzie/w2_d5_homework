import unittest
from classes.guest import Guest

class TestGuest (unittest.TestCase):

    def test_guest_has_name(self):
        self.assertEqual("Alice", Guest("Alice").name)