import requests
import json

CONFIG = {
    'url': 'http://api.daydayaup.com/product/product/productOffline?sign=7FC7E243BB29A07128C699F68F3BED96',
    'headers': {'Content-Type': 'application/json'}
}
data = {'ids': [
    
]}

url = CONFIG['url']
headers = CONFIG['headers']

response = requests.post(url=url, data=json.dumps(data), headers=headers, timeout=1)
print(response.content)
