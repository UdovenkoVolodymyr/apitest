import requests

#url = "https://apinlp-pro.herokuapp.com/messages"
url = "http://127.0.0.1:5000/messages"
req_str = "test_test_TEST"
response = requests.post(url, data=req_str, headers={"Content-Type": "text/plain"})
#response = requests.get(url)
print(response.text)
