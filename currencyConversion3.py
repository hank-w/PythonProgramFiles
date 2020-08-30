import requests
import csv
from collections import defaultdict

VALID_ACTIONS = {
	'CREATE': (None,),
	'FINALIZE': ('CREATE',),
	'PAY': ('FINALIZE', 'PAY',),
}

exchange_rate = None

def getExchangeRate():
	r = requests.get('https://api.exchangeratesapi.io/latest?base=USD')
	return r.json().get('rates', {})

def owing(billing_strings):
	global exchange_rate
	if exchange_rate is None:
		exchange_rate = getExchangeRate()

	if(billing_strings == [] or billing_strings == None):
		return 0

	

	id_to_current_action = defaultdict(lambda: None)
	id_to_balence = defaultdict(int)
	for invoice in billing_strings:
		action, id, amount, currency = invoice.split(', ')
		amount = float(amount)	

		if(currency != 'USD'):
			amount /= exchange_rate[currency]

		previous_action = id_to_current_action.get(id, None)
		#previous_action = id_to_current_action[id]

		if action not in VALID_ACTIONS or previous_action not in VALID_ACTIONS[action]:
			continue

		id_to_current_action[id] = action	

		if(action == 'FINALIZE'):
			id_to_balence[id] += amount

		if(action == 'PAY'):
			id_to_balence[id] -= amount

	return id_to_balence

billing_strings = [
  "CREATE, 100, 100, USD",
  "FINALIZE, 100, 100, USD",
  "PAY, 100, 100, USD",
  "CREATE, 10, 10, CAD",
  "FINALIZE, 10, 10, CAD",
  "PAY, 10, 5, CAD",
  "PAY, 10, 0, CAD",
  "CREATE, 11, 10, GBP",
  "FINALIZE, 11, 10, GBP",
  "PAY, 11, 5, GBP",
  "PAY, 11, 0, GBP",
]

print(owing(billing_strings))