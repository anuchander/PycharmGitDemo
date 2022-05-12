import requests
import json

uri="https://jsonplaceholder.typicode.com"
end_point="/users"
base_uri=uri+end_point

response=requests.get(base_uri)
json_response=json.loads(response.text)
new_json_response=json.dumps(json_response, indent=2)
print(new_json_response)
expected_name="Leanne Graham"
for data in json_response:
    #print(data['address'])
    assert expected_name in data['name']
    print(data)
    print(data['id'], data['name'], data['username'], data['email'], data['address']['geo'])








