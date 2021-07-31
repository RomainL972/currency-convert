#!/usr/bin/env python3

import requests
from dateutil.parser import parse
import os
import dotenv

dotenv.load_dotenv()

api_key = os.environ["API_KEY"]

def main():
    fromcur = input("From currency : ")
    tocur = input("To currency : ")
    amount = float(input("Amount : "))
    date = input("Date : ")
    if not date:
        date = "latest"

    params = {"access_key": api_key, "symbols": fromcur + "," + tocur}
    
    res = requests.get("http://data.fixer.io/api/" + date, params=params)
    data = res.json()
    rates = data["rates"]
    converted = amount / rates[fromcur] * rates[tocur]

    print("{} {} = {} {}".format(amount, fromcur, converted, tocur))

if __name__ == "__main__":
    main()
