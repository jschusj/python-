import xlrd


def get_skus():
    # 打开文件
    # workbook = xlrd.open_workbook(r'C:\Users\Administrator\Documents\WeChat Files\YTJSTAO\Files\YeePay_Transfer_2018-10-23.xls')
    workbook = xlrd.open_workbook(r'D:\1022.xlsx')
    # 获取所有sheet
    sheet = workbook.sheet_by_index(0)
    cols_0_list = sheet.col_values(1)
    business_no = ""
    for i in range(0, len(cols_0_list)):
        business_no = business_no + "L," + cols_0_list[i]
    print(business_no[1:])


if __name__ == '__main__':
    get_skus()
