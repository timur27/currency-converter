class Converter:
    def __init__(self):
        self.fxRates = {('EUR', 'USD'): 1.8}

    def convert(self, input, currency, target_currency):
        rate = self.fxRates[(currency, target_currency)]
        return rate * input
