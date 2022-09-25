from dotenv import load_dotenv
import datetime
import argparse
import requests
import json
import os

if __name__ == '__main__':
    # load key environment variable
    load_dotenv()
    key = os.getenv("KEY")

    # parse input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('amount', help='amount to be converted', type=float)
    parser.add_argument(
        'from_currency', help='base currency, typically your home currency', type=str)
    parser.add_argument(
        'to_currency', help='currency to convert to, output', type=str)
    parser.add_argument(
        '-d', '--date', help='select a specific date YYYY-MM-DD, defaults to today', type=str)
    parser.add_argument(
        '-v', '--verbose', help='include more detailed output, defaults to amount only', action="store_true")
    args = parser.parse_args()

    with open('symbols.json') as f:
        symbols = json.load(f)

    # verify that API supports the provided symbols, otherwise raise an error
    if args.from_currency not in symbols.keys() or args.to_currency not in symbols.keys():
        raise argparse.ArgumentTypeError(
            "must pass a valid symbol, refer to symbols.json")

    # store input varaiables
    date = args.date if args.date else datetime.date.today().isoformat()  # YYYY-MM-DD
    from_ = args.from_currency
    to_ = args.to_currency
    amount = args.amount

    url = f"https://api.apilayer.com/fixer/convert?to={to_}&from={from_}&date={date}&amount={amount}"

    payload = {}
    headers = {
        'apikey': key
    }

    # make request to the API
    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code

    data = response.json()

    if not args.verbose:
        result = data["result"]
        print(result)
    else:
        print(f'date: {data["date"]}')
        print(f'rate: {data["info"]["rate"]}')
        print(f'amount: {data["query"]["amount"]}')
        print(f'from: {from_} "{symbols[from_]}"')
        print(f'to: {to_} "{symbols[to_]}"')
        print(f'result: {data["result"]}')
