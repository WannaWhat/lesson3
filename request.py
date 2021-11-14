import requests

print('Get request example')
response = requests.get('http://localhost/headers')
print(response)
print(response.headers)
print(response.json())

print('\n\nPut request example')
response = requests.put('http://localhost/put/Petya', json={'age': 12})
print(response)
print(response.content)

print('\n\nDelete request example')
response = requests.delete('http://localhost/delete/Petya')
print(response)
print(response.content)

print('\n\nPost request example')
response = requests.post('http://localhost/post', json={'x': 12, 'y': 3})
if response.status_code == 200:
    print(response.json()['answer'])
elif response.status_code == 400:
    print(response.json()['exception'])
else:
    print('Unknown error')


print('\n\nGet headers example')
response = requests.get('http://localhost/headers')
print(response.status_code)
print(response.content)
print(response.headers)
