import requests
from bs4 import BeautifulSoup

headers = {
    'Host': 'www.zhihu.com',
    'Referer': 'https://www.zhihu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 '
                  'Safari/537.36 '
}

response = requests.get('https://www.zhihu.com/question/68295490', headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
imgs = soup.find_all('img')
for img in imgs:
    src = img.attrs['src']
    if src.startswith('data'):
        continue
    print(src)


