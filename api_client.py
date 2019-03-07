import requests
import json

# url = "https://apinlp-pro.herokuapp.com/messages"
#url = "http://127.0.0.1:5000/messages"
#input_str = "example str TEST"

#headers = {'Content-type': 'text/plain'}
#response = requests.request(method="GET", url=url, data=input_str, headers=headers)
#response = requests.post(url, data=req_str, headers=headers)

#print(response.text)


class outh(object):

    def __init__(self, login, password):
        self.password = password
        self.login = login

    def admit (self):
        logpas = {"login": self.login, "password": self.password}
        url = "http://127.0.0.1:5000/login"
        response = requests.request(method="GET",
                                    url=url,
                                    data=json.dumps(logpas),
                                    headers={'Content-type': 'application/json'})
        return response.text


test = outh(login='admin', password='123')
print(test.admit())

'''class VovaApi(object):

    def __init__(self, ):'''