'''
String s = "https://jsonplaceholder.typicode.com";
String s = "https://api.publicapis.org/entries";
'''
import requests
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


uri = "https://api.publicapis.org/entries"
response = requests.get(uri)
print(response.status_code)
#print(response.text)
data=json.loads(response.text)
print(type(data))
print(data['count'])
#print(data)

new_data = json.dumps(data, indent=2)
#print(new_data)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

with open("entries.json") as f:
    json_response=json.load(f)
    print(json_response['count'])
    for item in json_response['entries']:
        if item['API']=='Cat Facts':
            print(item['API'], "  ", item['Description'], "  ", item['Link'])
            driver.get(item['Link'])


