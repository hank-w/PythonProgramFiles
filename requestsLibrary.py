import requests, json

payload = {'page': 3, 'count': 25}
payload2 = {'username': 'billy', 'password': 'ron'}

r = requests.get('https://en.wikipedia.org/wiki/Yu-Gi-Oh!_5D%27s')
r2 = requests.get('https://upload.wikimedia.org/wikipedia/en/9/99/Yu-Gi-Oh_5D%27s_Volume_1_Cover.jpg')
r3 = requests.get('https://httpbin.org/get', params=payload)
r6 = requests.post('https://httpbin.org/post', data=payload2)
r7 = requests.get('https://httpbin.org/basic-auth/billy/ron', auth=('billy', 'ron'))
r9 = requests.get('https://httpbin.org/delay/1', timeout=3) #timeout to break out inf loop, delay for delayed content

article = r.text
pic = r2.content

#print(article)

#with open('goingFast.png', 'wb') as f:
#	f.write(pic)

#print(r.headers)
#print(r.status_code)

#print(r3.text)

#print (r6.status_code)
#print(r6.text)

#print(r6.json())
#r6_dict = r6.json()
#print(r6_dict['form'])

#print(r7.text)
#print(r7) #response code

print(r9)





























