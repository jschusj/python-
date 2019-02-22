import requests

import requests
import csv
import time
import subprocess as sp
import re


def fetch(url,proxy=None):
    """模拟浏览器打开网页"""
    s = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0",
        "Refere":"http://www.xicidaili.com/nn"
    }
    s.headers.update(headers)
    proxies = {}.fromkeys(["http","https"],f"{proxy[0]}:{proxy[1]}")if proxy else None#当proxy(即用户代理)不为None时，创建一个字典包含两个元素，分别以"http","https"为键。
                                                                                      #proxy[0]为IP,proxy[1]为端口
    return s.get(url,timeout=8,proxies=proxies,headers=headers).text

if __name__ == '__main__':
    html = fetch("https://www.xicidaili.com/nn/")
    print(html)