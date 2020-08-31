# https://www.youtube.com/watch?v=1lxrb_ezP-g
# https://www.youtube.com/watch?v=th5_9woFJmk
import json

import time
import requests
#stripe.api_key = 'sk_test_51HLaikGhktAqF47YE9lZ56FNWwGRiKMQ6lcTJRBOCZAnT9aWkQMZvD78KBz6uIdpVF8TIYh5NDX7uj8pyljYaElu00noE3XzIm'
#stripe.api_version = "2020-08-27"
r = requests.get('https://formulae.brew.sh/api/formula.json')

packages_json = r.json()

#print(len(packages_json))

packages_string = json.dumps(packages_json[0], indent=2)

package_name = packages_json[0]['name']
package_desc = packages_json[0]['desc']

package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'

r2 = requests.get(package_url)

package_json = r2.json()

package_str = json.dumps(package_json, indent=2)

#print(package_str)

installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]
installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]

#print(package_name, package_desc, installs_30, installs_90, installs_365)
 
results = []
t1 = time.perf_counter()
 
for package in packages_json:
	package_name = package['name']
	package_desc = package['desc']

	package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'

	r = requests.get(package_url)
	package_json = r.json()

	installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
	installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]
	installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]

	#print(package_name, package_desc, installs_30, installs_90, installs_365)

	data = {
		'name': package_name,
		'desc': package_desc,
		'analytics': {
			'30d': installs_30,
			'90d': installs_90,
			'365d': installs_365
		}
	}
	if(len(results) > 13):
		break
	results.append(data)
	time.sleep(r.elapsed.total_seconds())

	print(f'Got {package_name} in {r.elapsed.total_seconds()} seconds')

# break

t2 = time.perf_counter()
print(f'finished in {t2 - t1} seconds')
#print(results)

with open ('package_info.json', 'w') as f:
	json.dump(results, f, indent =2)
