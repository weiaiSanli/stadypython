import requests

# http://www.test.julongdata.com:8081/pgs/mobileapi/v1/pointsMall/pointTurnover?offset=0&time=2019-09&pageSize=10
url = "http://www.test.julongdata.com:8081/pgs/mobileapi/v1/pointsMall/pointTurnover"
head = {'userKey': 'd10deaeb-dee9-4b32-adb5-45587bc0b5a7'}
parms = {"offset":0 , "time":"2019-09" ,"pageSize": 10 }
r=requests.get(url , params = parms , headers = head)
print(r.text)