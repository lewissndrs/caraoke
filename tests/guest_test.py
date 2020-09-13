import unittest
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Song 2","Blur")
        self.guest1 = Guest("Frodo",20.0,self.song1)

    def test_guest_has_name(self):
        self.assertEqual("Frodo",self.guest1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(20.0,self.guest1.wallet)

    def test_reduce_wallet(self):
        self.guest1.reduce_wallet(10.0)
        self.assertEqual(10.0,self.guest1.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Song 2",self.guest1.fav_song.title)