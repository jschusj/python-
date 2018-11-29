import requests

headers = {
    'Origin': 'http://localhost:8200',
    'Authorization': '19255cab6c1513b56653ef77a5f09bab',
    'Access-Control-Allow-Methods': '*',
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Accept': 'application/json',
    'Referer': 'http://localhost:8200/',
    'Access-Control-Allow-Credentials': 'true',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Access-Control-Allow-Headers': '*',
}

params = (
    ('sign', 'C410CF9B38FF599BFBACE0D3FAFEBA79'),
)

data = '{"id":16,"state":false}'

response = requests.post('http://localhost:8000/creditMarket/update', headers=headers, params=params, data=data)
print(response.text)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('http://test.daydayaup.com:6979/user/creditMarket/update?sign=C410CF9B38FF599BFBACE0D3FAFEBA79', headers=headers, data=data)
