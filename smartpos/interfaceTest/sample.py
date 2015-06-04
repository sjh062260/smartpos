'''_
_author__ = 'jiaohui'
'''
import requests
import collections
import json

url = 'http://172.16.1.201:8080/merchant/login.json'
headers = {'x-app':'smart-pos','x-version':'10','x-deviceId':'k-201','x-sign':'08216bc91cb64412848317903070f9e3'}
pyload = {'loginName':'01400028','password':'888888'}

resp = requests.post(url,data=pyload,headers=headers)
resp_json = resp.json()
resp_data = json.loads(resp.content)

print(resp_data)
