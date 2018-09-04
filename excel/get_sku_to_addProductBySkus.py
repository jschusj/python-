import xlrd


def get_skus():
    # 打开文件
    # workbook = xlrd.open_workbook(r'F:\Work\Document\选品\UP选品\家居日用、家纺、服饰内衣.xlsx')
    # workbook = xlrd.open_workbook(r'F:\Work\Document\选品\UP选品\家具、家装建材、鞋靴.xlsx')
    # workbook = xlrd.open_workbook(r'F:\Work\Document\选品\UP选品\美妆护肤、礼品箱包、运动户外.xlsx')
    # workbook = xlrd.open_workbook(r'F:\Work\Document\选品\UP选品\手机、家用电器.xlsx')
    # workbook = xlrd.open_workbook(r'F:\Work\Document\选品\UP选品\数码、电脑办公.xlsx')
    # workbook = xlrd.open_workbook(r'F:\Work\Document\选品\UP选品\钟表、珠宝.xlsx')
    # workbook = xlrd.open_workbook(r'F:\Work\Document\选品\UP选品\钟表、珠宝.xlsx')
    workbook = xlrd.open_workbook(r'F:\Work\Document\选品\阿噗第一次选品.xlsx')
    # 获取所有sheet
    sheet = workbook.sheet_by_index(2)
    cols_0_list = sheet.col_values(0)
    skus = ""
    for i in range(1, len(cols_0_list)):
        # skus = skus + "," + cols_0_list[i]
        skus = skus + "," + cols_0_list[i]
    print(skus[1:])


if __name__ == '__main__':
    get_skus()
