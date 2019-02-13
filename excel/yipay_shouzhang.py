import xlrd


def get_skus():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\Users\Administrator\Documents\WeChat Files\YTJSTAO\Files\10023604549_20181227152132.xlsx')
    # 获取所有sheet
    sheet = workbook.sheet_by_index(0)
    # cols_0_list = sheet.col_values(0)
    cols_0_list = sheet.col_values(8)
    skus = ""
    for i in range(1, len(cols_0_list)):
        # skus = skus + "," + cols_0_list[i]
        item = cols_0_list[i]
        item = item.split(":")[0]
        # skus = skus + ",\"" + item + "\""
        skus = skus + "," + item + ""
    print(skus[1:])


if __name__ == '__main__':
    get_skus()
