import requests
import json
import jsonpath

baseuri="https://reqres.in"
endpoint="/api/users"
uri=baseuri+endpoint

def test_create_new_user():
    with open("/Users/anu/PycharmProjects/PycharmGitDemo/inputData/createuser.json") as f:
        read_json=json.load(f)
    response=requests.post(uri, read_json)
    print(response.text)
    assert response.status_code==202

def test_create_other_user():
     with open("/Users/anu/PycharmProjects/PycharmGitDemo/inputData/createuser.json") as f:
         read_json = json.load(f)
     response = requests.post(uri, read_json)
     print(response.text)
     assert response.status_code == 201
     json_response = json.loads(response.text)
     print(json_response['id'])
     id = jsonpath.jsonpath(json_response, 'id')
     print(id[0])



