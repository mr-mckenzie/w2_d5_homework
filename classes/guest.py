class Guest:
    def __init__(self, input_name, input_wallet):
        self.name = input_name
        self.wallet = input_wallet

    def pay_money(self, amount_to_pay):
        self.wallet -= amount_to_pay