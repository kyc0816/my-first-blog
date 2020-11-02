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
data = '1138.1111127.1111'

#2020 1102 post 아니고 get이라서 data 빼고 url만 넣었음
r=requests.get(url)
# r=requests.post(url, data=data)
print(3)
print(r)