import json


def convert():
    json_str = """
    {"AcceptStatus":"S","AppRetMsg":"交易成功","AppRetcode":"QT000000","InputCharset":"UTF-8","OrderTrxid":"101153500616268282742","PartnerId":"200001160097","PayTrxId":"301153500616267306763","RetCode":"S0001","RetMsg":"受理成功","Sign":"iShHChseqGV8+6ZNHqBVlQCdA1m8rQQ00NWweqA7yDnvIqmqEf/kqTfj2kcmqh9QcqLQNzZQnInmJ8WcV7R0Pqz+x67LR/I/x4HMR+uW4c/PLytdzfkZ806oc5C4v9NgP/1WJ5xHCO78a6TWiWJLFM5qAOw+VDyo7etkenBQTR4=","SignType":"RSA","Status":"S","TradeDate":"20180823","TradeTime":"143645","TrxId":"2017033311252304563042"}
    """
    josn_obj = json.loads(json_str)
    for key in josn_obj:
        print("private String " + key + ";")


if __name__ == '__main__':
    convert()
