class Guest:
    def __init__(self, input_name, input_wallet, input_favourite_song):
        self.name = input_name
        self.wallet = input_wallet
        self.favourite_song = input_favourite_song

    def pay_money(self, amount_to_pay):
        self.wallet -= amount_to_pay
    
    def react_to_playlist(self, play_list):
        for song in play_list:
            if song == self.favourite_song:
                return "Woopee!"
        
        return "blood-curdling scream"