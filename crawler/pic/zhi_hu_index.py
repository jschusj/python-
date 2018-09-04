import requests

headers = {
    'Host': 'www.zhihu.com',
    'Referer': 'https://www.zhihu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

params = (
    ('next', '/'),
)

response = requests.get('https://www.zhihu.com/signup', headers=headers, params=params)
print(response.encoding)
# response.encoding = 'gbk'
print(response.text)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.zhihu.com/signup?next=%2F', headers=headers)
