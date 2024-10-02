import requests

APP_URL = "https://todo.pixegami.io/"
response = requests.get(APP_URL)
status_code = response.status_code
assert status_code == 200
data = response.json()
print(data)
print(response.text)
print(type(response.headers))
#properties
print(response.headers)
print(response.url)
print(response.cookies)
print(response.encoding)
