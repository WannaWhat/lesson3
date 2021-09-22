import requests


response = requests.get('http://localhost/headers')
print(response)
print(response.headers)
print(response.json())

# response = requests.put('http://localhost/put/Petya', json={'age': 12})
# print(response)
# print(response.content)

response = requests.delete('http://localhost/delete/Petya')
print(response)
print(response.content)