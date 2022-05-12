import requests
import json
import jsonpath

baseuri="http://thetestingworldapi.com"
studentendpoint="/api/studentsDetails"
techskillsendpoint="/api/technicalskills"
addressendpoint="/api/addresses"
finaldetailsendpoint="api/FinalStudentDetails/1200207"

def test_add_new_student():
    uri=baseuri+studentendpoint
    with open("/Users/anu/PycharmProjects/PycharmGitDemo/inputData/createstudent.json") as f:
        input_json=json.load(f)
    response=requests.post(uri, input_json)
    assert response.status_code == 201
    print(response.text)
    idval=jsonpath.jsonpath(response.json(), 'id')
    print(idval[0])

    uri=baseuri+techskillsendpoint
    with open("/Users/anu/PycharmProjects/PycharmGitDemo/inputData/techskills.json") as f2:
        input2_json=json.load(f2)
    input2_json['id']=idval[0]
    input2_json['st_id']=idval[0]
    response=requests.post(uri, input2_json)
    print(response.text)

    uri = baseuri + addressendpoint
    with open("/Users/anu/PycharmProjects/PycharmGitDemo/inputData/address.json") as f:
        input_json = json.load(f)
    input2_json['st_id']=idval[0]
    response = requests.post(uri, input_json)
    print(response.text)
    print("address done!")

    final_details=baseuri+finaldetailsendpoint
    response=requests.get(final_details)
    print(response.text)
    print(response.status_code)
    print("Final results!")


