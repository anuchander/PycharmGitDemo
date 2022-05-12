import requests
import json
import jsonpath

url="https://reqres.in"
endpoint="/api/users?page=2"
baseuri=url+endpoint

response = requests.get(baseuri)

print("Printing json response")
json_response=json.loads(response.text)
print(type(json_response))
print(json_response)

print(type(json_response['data']))
for d in json_response['data']:
    #print(d) - prints the list as dictionary items
    del(d['avatar'])
    print(d['id'],d['first_name'], d['last_name'], d['email'])

print()
print("*********Converting python object to json string*********")
new_string=json.dumps(json_response, indent=2)
print(new_string)
