from dotenv import load_dotenv
from datetime import date
import argparse
import requests
import json
import os

if __name__ == '__main__':
    load_dotenv()
    key = os.getenv("KEY")

    today = date.today().isoformat()
    from_cur = "GBP"
    to_cur = "USD"
    amount = 10

    url = f"https://api.apilayer.com/fixer/convert?to={to_cur}&from={from_cur}&date={today}&amount={amount}"

    payload = {}
    headers = {
        'apikey': key
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code

    data = response.json()
    rate = data["info"]["rate"]
    result = data["result"]

    print(f"amount: {amount} rate: {rate} result: {result}")
