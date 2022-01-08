class Converter:
    def __init__(self):
        self.fx_rates = {('EUR', 'USD'): 1.8}

    def convert(self, input, currency, target_currency):
        rate = self.fx_rates[(currency, target_currency)]
        return rate * input
