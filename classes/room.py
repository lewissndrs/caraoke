class Room:

    def __init__(self,input_room_no,input_capacity):
        self.room_no = input_room_no
        self.capacity = input_capacity
        self.guests = []
        self.songs = []
        self.till = 0

    def check_guest_into_room(self,guest):
        if len(self.guests) < self.capacity:
          self.guests.append(guest)

    def check_guest_out_of_room(self,guest):
        self.guests.remove(guest)

    def add_song(self,song):
        self.songs.append(song)

    def check_fav_song(self,guest):
        for song in self.songs:
            if guest.fav_song.title == song.title:
               return "Oh now THIS is my JAM WHOO!"

    def take_entry(self,guest,fee):
        if guest.wallet >= fee:
            guest.reduce_wallet(fee)
            self.till += fee
