"""
import pandas as pd
# 输出 excel表格
data = pd.read_excel('data.xlsx')
print(data.values)

# 修改 excel表格内容
data = pd.read_excel('data.xlsx',sheet_name="登陆")
data["编号"][data["编号"] == 1] = 100
# 修改完，保存到 excel表格 sheet2里面
data.to_excel("data.xlsx", "Sheet2")
"""
import xlrd
def read_excel(excel_path,sheet_name,skip_first=True):
    results = []
    datas = xlrd.open_workbook(excel_path)
    table = datas.sheet_by_name(sheet_name)
    if skip_first == True:
        start_row = 1
    else:
        start_row = 0
    
    # 循环读取每一行的数据
    for row in range(start_row,table.nrows):
        results.append(table.row_values(row))
    return results

# print(read_excel("data.xlsx","Sheet"))
