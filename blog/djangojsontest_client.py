import requests  
import json

# **** sendTo = local
# url = "http://127.0.0.1:8000/service_learning/"

# **** sendTo = online
url = "http://kyc0816.pythonanywhere.com/service_learning/"

# **** dataType = JSON
# data = '{"GPS":"123, 456"}'
# headers = {'content-type': 'application/json'}
# r=requests.post(url, data=json.dumps(data), headers=headers)

# **** dataType = string
data = 'hi'
r=requests.post(url, data=data)

r.text