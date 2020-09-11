import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Videotape","Radiohead")

    def test_song_has_title(self):
        self.assertEqual("Videotape",self.song1.title)

    def test_song_has_artist(self):
        self.assertEqual("Radiohead",self.song1.artist)