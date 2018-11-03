import requests
import json

res = requests.get("http://www.mediosz.club:8083/web")
data = json.loads(res.text)
#print(data["result"])

for index, item in enumerate(data["result"]):
    print(item["url"])
    print(item["result"])
    print(item["status"])
    print(item["timestamp"])


pynq_res = requests.get("http://www.mediosz.club:8083/pynq")
pynq_data = json.loads(pynq_res.text)
print(pynq_data["result"])

result = {
    "url": "www.mesd",
    "res": "12321",
    "tes": "dasdas"
}

print(result)
print(json.dumps(result))
r = requests.post(url, data=result)