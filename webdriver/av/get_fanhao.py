import re

import requests

res = requests.get('http://www.manew.com/blog-166885-17920.html')
str = res.text
# print(str)
list = re.findall(r'[A-Z]+-', str)
result = []
for name in list:
    result.append(name[0: len(name) - 1])
print(result)

