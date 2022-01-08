import ConvertValue
import ConvertValueHandler


def run():
    command = ConvertValue.ConvertValue(1, 'EUR', 'USD')
    handler = ConvertValueHandler.ConvertValueHandler()
    print handler.handle(command)


if __name__ == '__main__':
    run()