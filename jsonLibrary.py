''' javaScript Object Notation '''

import json

people_string = '''
{
	"people": [
		{
			"name":"John Smith",
			"phone": "615-957-0913",
			"emails": ["billy@gmail.com, rat@gmail.com"],
			"has_license": false
		},
		{
			"name":"John Proctor",
			"phone": "619-957-0913",
			"emails": null,
			"has_license": true
		}
	]
}
'''

data = json.loads(people_string)

#print(data)
#print(type(data))
#print(data)

#print(type(data['people']))

#for person in data['people']:
#	print(person['name'], person['phone'])

for person in data['people']:
	del(person['phone'])

new_string = json.dumps(data, indent=2, sort_keys=True)#alphabetical sort of keys per entry

print(new_string)




