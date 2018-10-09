import _thread

import requests
import time


def confirm():
    data = {"payId": "1044500265391157250", "validateCode": "902653"}
    headers = {"Authorization": "cf9255ee333bfad573a1ca734f2cbef2"}
    res = requests.post("http://api.daydayaup.com:6979/pay/confirmPay?sign=CA91C60EE83B8A3415E290801B663723", data=data,
                        headers=headers)
    print(res.text)


if __name__ == '__main__':
    _thread.start_new(confirm, ())
    _thread.start_new(confirm, ())
    _thread.start_new(confirm, ())
    time.sleep(10)
