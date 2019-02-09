import requests  
import json
# url = "http://127.0.0.1:8000/service_learning/"
url = "http://kyc0816.pythonanywhere.com/service_learning/"
# data = '{"GPS":"123, 456"}'
# headers = {'content-type': 'application/json'}
data = 'hi'
# r=requests.post(url, data=json.dumps(data), headers=headers)
r=requests.post(url, data=data)
r.text