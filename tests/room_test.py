import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room(1,6)
        self.song1 = Song("Wouldn't it be nice","Beach Boys")
        self.song2 = Song("Hello Nasty","Beastie Boys")
        self.guest1 = Guest("Lewis Saunders",30.00,self.song2)

    def test_room_has_number(self):
        self.assertEquals(1, self.room1.room_no)

    def test_room_has_capacity(self):
        self.assertEqual(6, self.room1.capacity)

    def test_check_in(self):
        self.room1.check_guest_into_room(self.guest1)
        self.assertEqual(1,len(self.room1.guests))

    def test_check_out(self):
        self.room1.check_guest_into_room(self.guest1)
        self.room1.check_guest_into_room(self.guest1)
        self.room1.check_guest_out_of_room(self.guest1)
        self.assertEqual(1,len(self.room1.guests))

    def test_add_song(self):
        self.room1.add_song(self.song1)
        self.assertEqual(1,len(self.room1.songs))