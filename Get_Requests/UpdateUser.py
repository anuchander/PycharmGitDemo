import requests
import json
import jsonpath

baseuri="https://reqres.in"
endpoint="/api/users/2"
uri=baseuri+endpoint

with open("/inputData/createuser.json") as f:
    read_json=json.load(f)

response=requests.put(uri, read_json)
print(response.text)
assert response.status_code==200


#convert response data into json data for printing
json_response = json.loads(response.text)
print(json_response)
print()
print( "Printing individual data ")
print()
print(json_response['name'])
print(json_response['job'])
print(json_response['updatedAt'])

#print above data, id using jsonpath, returns an array even if single element

name=jsonpath.jsonpath(json_response, 'name')
job=jsonpath.jsonpath(json_response, 'job')
updated=jsonpath.jsonpath(json_response, 'updatedAt')
print(name[0], " ", job[0], " ", updated[0])

