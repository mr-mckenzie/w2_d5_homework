import unittest
from classes.song import Song

class TestSong (unittest.TestCase):

    def setUp(self):
        self.example_song = Song("Let It Be", "The Beatles", 4)

    def test_song_has_title(self):
        self.assertEqual("Let It Be", self.example_song.title)

    def test_song_has_artist(self):
        self.assertEqual("The Beatles", self.example_song.artist)

    def test_song_has_length(self):
        self.assertEqual(4, self.example_song.length)