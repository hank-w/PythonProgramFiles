import json 
import requests
import time

def install_sort(package):
	return package['analytics']['30d']

with open('package_info.json', 'r') as f:
	data = json.load(f)

#print(data)


#
data = [item for item in data if 'abc' in item['name']]

data.sort(key=install_sort, reverse=True)

data_str = json.dumps(data[:3], indent=2)
print(data_str)