import requests

html = requests.get('http://47.99.154.250:8889/ip', proxies={"http": "http://{}".format("111.177.168.115:9999")})
# html = requests.get('http://47.99.154.250:8889/ip')
print(html.content)
