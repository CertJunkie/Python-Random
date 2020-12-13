import requests

url = "https://sandboxsdwan.cisco.com:8443/dataservice/device"

payload = {}
headers = {
  'Cookie': 'JSESSIONID=MGCNHm18vTF7_qoM391_3NnziIszBLQNMWCg3xwF.4854266f-a8ad-4068-9651-d4e834384f51'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))





