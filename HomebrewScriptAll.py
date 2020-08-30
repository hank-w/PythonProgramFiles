import json
import requests

r = requests.get('https://formulae.brew.sh/api/formula.json')

packages_json = r.json()

print(packages_json)