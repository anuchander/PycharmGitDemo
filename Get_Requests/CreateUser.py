import requests
import json
import jsonpath

baseuri="https://reqres.in"
endpoint="/api/users"
uri=baseuri+endpoint

with open("/Users/anu/PycharmProjects/PycharmGitDemo/inputData/createuser.json") as f:
    read_json=json.load(f)

response=requests.post(uri, read_json)
print(response.text)
assert response.status_code==201
print("Printing response header")
print(response.headers)
print(response.headers.get('Content-length'), response.headers.get('Content-Type'))

#convert response data into json data for printing
json_response = json.loads(response.text)
print(json_response['id'])

#print above data, id using jsonpath, returns an array even if single element

id=jsonpath.jsonpath(json_response, 'id')
print(id[0])

