import unittest
from classes.guest import Guest
from classes.song import Song

class TestGuest (unittest.TestCase):

    def setUp(self):
        self.fav_song = Song("Enter Sandman", "Metallica", 5)
        self.non_fav_song = Song("West End Girls", "Pet Shop Boys", 5)
        self.guest = Guest("Alice", 50, self.fav_song)

    def test_guest_has_name(self):
        self.assertEqual("Alice", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(50, self.guest.wallet)

    def test_guest_pays_money(self):
        self.guest.pay_money(15)
        self.assertEqual(35, self.guest.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Enter Sandman", self.guest.favourite_song.title)

    def test_guest_reacts_to_playlist__fav(self):
        playlist = [self.non_fav_song, self.non_fav_song, self.fav_song]
        self.assertEqual("Woopee!", self.guest.react_to_playlist(playlist))

    def test_guest_reacts_to_playlist__non_fav(self):
        playlist = [self.non_fav_song, self.non_fav_song, self.non_fav_song]
        self.assertEqual("blood-curdling scream", self.guest.react_to_playlist(playlist))