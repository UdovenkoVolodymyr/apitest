import requests

#url = "https://apinlp-pro.herokuapp.com/messages"
url = "http://127.0.0.1:5000/messages"
input_str = "example str TEST"

headers = {'Content-type': 'text/plain'}
response = requests.request(method="GET", url=url, data=input_str, headers=headers)
#response = requests.post(url, data=req_str, headers=headers)

print(response.text)
