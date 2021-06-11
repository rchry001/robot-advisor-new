# this is the "app/robo_advisor.py" file

import os
from dotenv import load_dotenv
import requests

load_dotenv() # go get env vars from the .env file

# read env variables
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

# make a request

symbol = "VYM" # ask for a user input....Eventually could add a user input for risk tolerance and investment time horizon

# Information input requirement: Set up user choice to make user pick a stock

user_choice = input("Please enter a ticker symbol, or multiple symbols, to view information:")
print("TICKER SYMBOL SELECTED: ", user_choice)


#
# 
# Validation requirement: to prevent an error if stock ticker symbol is likely invalid
# Logic: If what is entered is > than 4 characters then try again, if < than 1 character try again

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"

# response is a command used as part of the requests package

response = requests.get(request_url)
print(type(response))
print(response.text)
