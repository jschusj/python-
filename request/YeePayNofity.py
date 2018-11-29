import time

import requests
import re

file = open(r'C:\Users\Administrator\Desktop\log\2018-11\pay\upmall-provider-pay_shot.2018-11-15.log','r', encoding='UTF-8')
lines = file.readlines()
for line in lines:
    line = line.strip('\n')
    if "回调解密失败->merchantNo" in line:
        print(line)
        merchantNo = re.findall("merchantNo=.*,businessType", line)[0]
        merchantNo = merchantNo[11:22]
        print(merchantNo)
        businessType = re.findall("businessType=.*,encryptRes", line)[0]
        if 'memberOpen' in businessType:
            businessType = businessType[13:23]
        else:
            businessType = businessType[13:22]
        print(businessType)
        encryptRes = re.findall("encryptRes.*", line)[0]
        encryptRes = encryptRes[11:]
        print(encryptRes)
        data = {
            "businessType": businessType,
            "merchantNo": merchantNo,
            "response": encryptRes
        }
        res = requests.post("http://api.daydayaup.com/pay/notify/yeePayNotify", data=data)
        print(res.text)
        time.sleep(5)

