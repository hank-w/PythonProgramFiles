#!/usr/bin/env python

from collections import defaultdict
import requests
import csv

"""
Write a program that takes in list strings with billing info: action(CREATE, FINALIZE, PAY), id, amount, currency. Invoice can not be paid if it was finalized or created. It can not be finalized if it wasn't created. For all the invoices in USD, you have to return the total amount that is being owed (created + finalized).
"""

VALID_PREVIOUS_ACTIONS = {
  'CREATE': (None,),
  'FINALIZE': ('CREATE',),
  'PAY': ('FINALIZE', 'PAY'),
}

exchange_rates = None

def get_exchange_rates():
  response = requests.get("https://api.exchangeratesapi.io/latest?base=USD")
  return response.json().get('rates', {})

def owing(billing_strings):
  global exchange_rates
  if exchange_rates is None:
    exchange_rates = get_exchange_rates()

  id_to_current_action = defaultdict(lambda: None)
  id_to_balance = defaultdict(int)
  for billing_string in billing_strings:
    action, id_, amount, currency = billing_string.split(', ')
    amount = float(amount)
    
    if currency != 'USD':
      try:
        amount /= exchange_rates[currency]
      except KeyError:
        print('Unknown currency:', currency)
        continue
    previous_action = id_to_current_action[id_]
    if action not in VALID_PREVIOUS_ACTIONS or previous_action not in VALID_PREVIOUS_ACTIONS[action]:
      # invalid or out of order, skip
      continue
    id_to_current_action[id_] = action
    if action == 'FINALIZE':
      id_to_balance[id_] = amount
    elif action == 'PAY':
      id_to_balance[id_] -= amount
  
  return id_to_balance

billing_strings = [
  "CREATE, 100, 100, USD",
  "FINALIZE, 100, 100, USD",
  "PAY, 100, 100, USD",
  "CREATE, 10, 10, CAD",
  "FINALIZE, 10, 10, CAD",
  "PAY, 10, 5, CAD",
  "PAY, 10, 0, CAD",
  "CREATE, 10, 10, GBP",
  "FINALIZE, 10, 10, GBP",
  "PAY, 10, 5, GBP",
  "PAY, 10, 0, GBP",
]
id_to_balance = owing(billing_strings)

with open('answer.csv', 'w') as f:
  csvwriter = csv.writer(f)
  csvwriter.writerows([(id_, "%.2f" % balance) for id_, balance in id_to_balance.items()])
