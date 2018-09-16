import requests

headers = {
    'authority': 'safeurl.net',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': '__cfduid=dedfef34758c45fe85d483d7f9bfcacdf1537085008; _ga=GA1.2.348399243.1537085011; _gid=GA1.2.2047155859.1537085012',
}

response = requests.get('https://safeurl.net/l/AB9')
print(response.text) # <a onclick="window.open('https://newtabz.stream/1Vdcs:ZuNBQB','_blank');window.close();" class="waves-effect waves-light btn-large"><h5>ENTER</h5></a>
