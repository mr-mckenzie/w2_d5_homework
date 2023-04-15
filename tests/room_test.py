import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp (self):
        self.room = Room("CodeClan Caraoke", 8)

        self.first_guest = Guest("Brian", 220)
        self.second_guest = Guest("Charlotte", 17)

        self.song = Song("Wonderwall", "Oasis", 4)

    def test_room_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(8, self.room.capacity)
    
    def test_room_is_empty(self):
        self.assertEqual([], self.room.guest_list)

    def test_room_has_no_songs(self):
        self.assertEqual([], self.room.playlist)

    def test_guest_check_in__enough_money(self):
        self.room.check_guest_in(self.first_guest, 20)
        self.assertEqual([self.first_guest], self.room.guest_list)
        self.assertEqual(200, self.first_guest.wallet)

    def test_guest_check_in__not_enough_money(self):
        self.room.check_guest_in(self.second_guest, 20)
        self.assertEqual([], self.room.guest_list)
        self.assertEqual(17, self.second_guest.wallet)

    def test_guest_check_out(self):
        self.room.check_guest_in(self.first_guest, 10)
        self.room.check_guest_in(self.second_guest, 10)
        self.room.check_guest_out(self.first_guest)
        self.assertEqual([self.second_guest], self.room.guest_list)

    def test_check_out_guest_not_in_guest_list(self):
        self.assertEqual(None, self.room.check_guest_out(self.second_guest))
        self.assertEqual([], self.room.guest_list)
    
    def test_add_song_to_playlist(self):
        self.room.add_song(self.song)
        self.assertEqual([self.song], self.room.playlist)

    def test_room_max_capacity(self):
        #check in 10 guests to a room with a capacity of 8
        for i in range(10):
            self.room.check_guest_in(self.first_guest, 10)

        self.assertEqual(8, len(self.room.guest_list))