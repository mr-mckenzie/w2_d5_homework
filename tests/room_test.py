import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp (self):
        self.room = Room("CodeClan Caraoke")

        self.first_guest = Guest("Brian")
        self.second_guest = Guest("Charlotte")

        self.song = Song("Wonderwall", "Oasis", 4)

    def test_room_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.room.name)
    
    def test_room_is_empty(self):
        self.assertEqual([], self.room.guest_list)

    def test_room_has_no_songs(self):
        self.assertEqual([], self.room.playlist)

    def test_guest_check_in(self):
        self.room.check_guest_in(self.first_guest)
        self.assertEqual([self.first_guest], self.room.guest_list)

    def test_guest_check_out(self):
        self.room.check_guest_in(self.first_guest)
        self.room.check_guest_in(self.second_guest)
        self.room.check_guest_out(self.first_guest)
        self.assertEqual([self.second_guest], self.room.guest_list)

    def test_check_out_guest_not_in_guest_list(self):
        self.assertEqual(None, self.room.check_guest_out(self.second_guest))
        self.assertEqual([], self.room.guest_list)
    
    def test_add_song_to_playlist(self):
        self.room.add_song(self.song)
        self.assertEqual([self.song], self.room.playlist)
