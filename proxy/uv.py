import requests


def get_proxy():
    return requests.get("http://www.tianba.online:8080/get/").content


def delete_proxy(proxy):
    requests.get("http://www.tianba.online:8080/delete/?proxy={}".format(proxy))


# your spider code

def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy()
    print(proxy)
    while retry_count > 0:
        try:
            # html = requests.get('http://www.tianba.online/')
            html = requests.get('http://www.tianba.online/', proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    delete_proxy(proxy)
    return None


if __name__ == '__main__':
    while True:
        print(getHtml())
