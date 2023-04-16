import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp (self):
        self.room = Room("CodeClan Caraoke", 8)

        self.song_one = Song("Dancing Queen", "ABBA", 4)
        self.song_two = Song("Wonderwall", "Oasis", 4)

        self.first_guest = Guest("Brian", 220, self.song_one)
        self.second_guest = Guest("Charlotte", 17, self.song_two)


    def test_room_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(8, self.room.capacity)
    
    def test_room_is_empty(self):
        self.assertEqual([], self.room.guest_list)

    def test_room_has_no_songs(self):
        self.assertEqual([], self.room.playlist)

    def test_room_has_tab(self):
        self.assertEqual({}, self.room.tab)

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
        self.room.add_song(self.song_one)
        self.assertEqual([self.song_one], self.room.playlist)

    def test_room_max_capacity(self):
        #attempt to check in 10 guests to a room with a capacity of 8
        for i in range(10):
            self.room.check_guest_in(self.first_guest, 10)

        self.assertEqual(8, len(self.room.guest_list))

    def test_guests_check_playlist(self):
        self.room.add_song(self.song_one)
        self.room.add_song(self.song_one)
        self.assertEqual("Woopee!", self.first_guest.react_to_playlist(self.room.playlist))
        self.assertEqual("blood-curdling scream", self.second_guest.react_to_playlist(self.room.playlist))

    def test_add_to_tab__successful(self):
        self.room.add_to_tab("beer", self.first_guest)
        self.room.add_to_tab("wine", self.first_guest)
        self.assertEqual(11, self.room.tab[self.first_guest.name])
        self.assertEqual(209, self.first_guest.wallet)

    def test_add_to_tab__item_not_on_menu(self):
        add_to_tab = self.room.add_to_tab("t-shirt", self.first_guest)
        #make sure function returns 'None'
        self.assertEqual(None, add_to_tab)
        #and no money is taken out of guest's wallet
        self.assertEqual(220, self.first_guest.wallet)

    def test_add_to_tab__wallet_is_empty(self):
        self.room.add_to_tab("beer", self.second_guest)
        self.room.add_to_tab("burger", self.second_guest)
        add_to_tab = self.room.add_to_tab("inflatable microphone", self.second_guest)
        #make sure function returns 'None'
        self.assertEqual(None, add_to_tab)
        #make sure earlier tab items added correctly
        self.assertEqual(15, self.room.tab[self.second_guest.name])
        #and no money is taken out of guest's wallet for unaffordable item
        self.assertEqual(2, self.second_guest.wallet)