import argparse

from stocks_cli import Stock

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('symbol', metavar='symbol')
    parser.add_argument('--api-key', metavar='api_key')

    print(parser.parse_args())
    args = parser.parse_args()
    print(Stock.get(args.symbol, args.api_key))