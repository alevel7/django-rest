import requests
from requests import Response

endpoint:str = 'http://localhost:8000/api/'
endpoint1:str = 'https://httpbin.org/anything'

response: Response = requests.get(endpoint, json={}, params={"name":"kazeem"})
print(response.text)
print(response.status_code)