import Converter


class ConvertValueHandler:
    def __init__(self):
        self.converter = Converter.Converter()

    def handle(self, command):
        return self.converter.convert(command.input, command.currency, command.target_currency)
