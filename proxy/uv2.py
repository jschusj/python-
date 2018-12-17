import requests

html = requests.get('http://www.tianba.online/', proxies={"http": "http://{}".format("222.171.251.43:40149")})
# html = requests.get('http://www.tianba.online/')
print(html.content)
