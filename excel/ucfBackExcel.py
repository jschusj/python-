import xlrd


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'F:\Work\Document\pay\先锋支付\先锋支付\机构编码列表--2018.05.10.xlsx')
    # 获取所有sheet
    # print(workbook.sheet_names())
    sheet = workbook.sheet_by_index(0)

    cols_0_list = sheet.col_values(0)
    # print(cols_0_list)
    cols_1_list = sheet.col_values(1)
    # print(cols_1_list)

    for i in range(1, len(cols_0_list)):
        print('map.put("' + cols_1_list[i] + '", "' + cols_0_list[i] + '");')


if __name__ == '__main__':
    read_excel()
