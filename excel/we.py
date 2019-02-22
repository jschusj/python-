import xlrd


def get_skus():
    # 打开文件
    # workbook = xlrd.open_workbook(r'C:\Users\Administrator\Documents\WeChat Files\YTJSTAO\Files\YeePay_Transfer_2018-10-23.xls')
    workbook = xlrd.open_workbook(r'C:\Users\Administrator\Documents\WeChat Files\YTJSTAO\Files\4、应收账款转让清单（债转清单）2019-02-21.xls')
    # 获取所有sheet
    sheet = workbook.sheet_by_index(0)
    cols_0_list = sheet.col_values(1)
    business_no_all = ""
    for i in range(1, len(cols_0_list)):
        business_no = cols_0_list[i]
        business_no_all = business_no_all + business_no + "L,"
    print(business_no_all)


if __name__ == '__main__':
    get_skus()
