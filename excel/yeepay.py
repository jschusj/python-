import xlrd


def get_skus():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\Users\Administrator\Documents\WeChat Files\YTJSTAO\Files\YeePay_Transfer_2018-10-18.xls')
    # 获取所有sheet
    sheet = workbook.sheet_by_index(0)
    cols_0_list = sheet.col_values(0)
    business_no = ""
    for i in range(3, len(cols_0_list)):
        business_no = business_no + "," + cols_0_list[i]
    print(business_no[1:])


if __name__ == '__main__':
    get_skus()
