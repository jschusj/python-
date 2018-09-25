import requests

headers = {
    'cookie': '__cfduid=dba77d8224449ea9b59facb40478919481536124961; _ga=GA1.2.1725626148.1536124966; _gid=GA1.2.1712201167.1536124966; musicLang=en',
    # 'origin': 'https://my-free-mp3.net',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    # 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'referer': 'https://my-free-mp3.net/cn',
    # 'authority': 'my-free-mp3.net',
    'x-requested-with': 'XMLHttpRequest',
}
# https://my-free-mp3.net/api/search.php?callback=jQuery21306259021800641733_1536131034623
params = (
    ('callback', 'jQuery21306259021800641733_1536131034623'),
)

data = [
  ('q', 'bb'),
  ('page', '0'),
]

response = requests.post('https://my-free-mp3.net/api/search.php', headers=headers, params=params, data=data)
print(response.text)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://my-free-mp3.net/api/search.php?callback=jQuery21309269047646307997_1536124992757', headers=headers, data=data)
