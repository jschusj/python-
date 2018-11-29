import requests

headers = {
    'Origin': 'http://localhost:8200',
    'Authorization': 'SYSTEM_LOGIN_TOKEN_dde7ff0f330aca953131f6af3a754076',
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
    ('sign', 'C397ECAF1060279A3B0E423E3D8C98AF'),
)

data = '{"ids":["1063314196493549570"],"source":"up"}'

response = requests.post('http://test.daydayaup.com:6979/pay/topup', headers=headers, params=params, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('http://test.daydayaup.com:6979/pay/topup?sign=C397ECAF1060279A3B0E423E3D8C98AF', headers=headers, data=data)
