import requests
import json


baseuri="https://reqres.in"
endpoint="/api/users/2"
uri=baseuri+endpoint

response = requests.delete(uri)
print(response.status_code)
