import json
#json.load/loads - covert to python object/python string
#json.dump/dumps - convert to json file/json string

with open('states.json') as f:
	data = json.load(f)
#print(data)

#for state in data['states']:
	#print(state)
	#print(state['name'], state['abbreviation'])

for state in data['states']:
	del state['area_codes']

with open('new_states.json', 'w') as f:
	json.dump(data, f, indent=2)	

