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

resp_data = resp.json()
respData = resp_data['data']
sessionId = respData['sessionId']

handover_url = 'http://172.16.1.201:8080/handover/statistics,json'
headersHandover= headers.update(other=['x-sessionId':sessionId])
headoverData = {'startTime':'2015-05-10 17:34:58','endTime':'2015-05-16 17:34:58'}
resp_handover = requests.post(handover_url,data=handoverData,headers=headers)


print(resp_data)
print respData
print sessionId
print(resp_handover)

