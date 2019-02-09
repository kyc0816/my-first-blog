import requests  
import json
url = "http://127.0.0.1:8000/service_learning/"
data = {"GPS":"123, 456"}
headers = {'content-type': 'application/json'}
r=requests.post(url, data=json.dumps(data), headers=headers)
r.text