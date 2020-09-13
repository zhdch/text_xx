# 必须要到 requests_zdh文件夹下运行
import requests
from dbtools import query   # 直接调 pymysql连接数据库的方法
from xlrd_tools import read_excel   #  用 xlrd调 excel表格内容
exl = read_excel("data.xlsx","Sheet")
print(exl[0][2])

# 有参数的 post接口
url = exl[0][2]
data = eval(exl[0][5])      # eval类的转换
h = eval(exl[0][4])       # eval 类的转换
res = requests.post(url=url,json=data,headers=h)
print(res.text)
assert res.status_code == 200
assert res.json()["status"] == 200
sql = "select * from t_user where username = 'zhdch'"
assert len(query(sql)) != 0
print("接口测试成功")

# 数据和脚本的分离，数据存放在 excel中，通过 pandas读取出来
"""
token = res.json()["data"]["token"]
url1 = "http://118.24.105.78:2333/inspirer/new"
headers1 = {"Content-Type":"application/json", "token":token}
data1 = {"content":"内1111111容"}
res1 = requests.post(url=url1,json=data1,headers=headers1)
print(res1.text)
assert res1.status_code == 200
assert res1.json()["status"] == 200
sql1 = "select * from t_inspirer where content = '内1111111容'"
assert len(query(sql1)) != 0
print("发表灵感成功")
"""