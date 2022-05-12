import requests
import json
import jsonpath

url="https://reqres.in"
endpoint="/api/users?page=2"
baseuri=url+endpoint

response = requests.get(baseuri)
print(response.content)
print(response.status_code)
print(response.headers)
print()
print("Printing json response")
json_response=json.loads(response.text)
print(json_response)
print()
print("Print jsonpath data ")
pages=jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])
assert pages[0]==2

print("Getting Firstname, lastname, email address")
print(json_response['data'][0]['first_name'], " ", json_response['data'][0]['last_name'], " ", json_response['data'][0]['email'], )





