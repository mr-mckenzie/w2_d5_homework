class Room:

    def __init__(self, input_room_name, input_capacity):
        self.name = input_room_name
        self.capacity = input_capacity
        self.guest_list = []
        self.playlist = []

    def check_guest_in(self, guest_to_enter, check_in_price):
        if len(self.guest_list) < self.capacity and guest_to_enter.wallet >= check_in_price:
            guest_to_enter.pay_money(check_in_price)
            self.guest_list.append(guest_to_enter)

    def check_guest_out(self, guest_to_leave):
        if guest_to_leave in self.guest_list:
            for guest in self.guest_list:
                if guest == guest_to_leave:
                    self.guest_list.remove(guest_to_leave)

    def add_song(self, song_to_add):
        self.playlist.append(song_to_add)