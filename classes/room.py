class Room:

    def __init__(self,input_room_no,input_capacity):
        self.room_no = input_room_no
        self.capacity = input_capacity
        self.guests = []
        self.songs = []

    def check_guest_into_room(self,guest):
        self.guests.append(guest)

    def check_guest_out_of_room(self,guest):
        self.guests.remove(guest)

    def add_song(self,song):
        self.songs.append(song)