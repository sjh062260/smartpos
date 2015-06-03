'''_
_author__ = 'jiaohui'
'''
import requests
import collections
import json

url = 'http://172.16.1.6:8080/merchant/login.json'
headers = {'x-app':'smart-pos','x-version':'10','x-deviceId':'k-201','x-sign':'08216bc91cb64412848317903070f9e3'}
pyload = {'loginName':'01400028','password':'888888'}

resp = requests.post(url,data=pyload,headers=headers)
resp_json = resp.json()
data_dict = resp_json["data"]

print resp.text
print(resp_json)
print(type(resp_json))
print(resp_json["data"])
print(type(data_dict))
print(data_dict['cashier'])
print(resp_json['data']['cashier'])
