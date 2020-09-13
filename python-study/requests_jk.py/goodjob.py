# 调接口
import requests
from dbtools import query   # 直接调 pymysql连接数据库的方法

# 1.构造请求
url = "http://118.24.105.78:2333/get_title_img"
r = requests.get(url)
print(r.text)     # 获取字符串形式的返回值

# 2.判断结果，断言实现判断http状态码，和结果码。
#  status：200 
#  判断语句：> < = != is in
assert r.status_code == 200  # 判断接口是否正常，获取http状态码
# r.json()把结果转化为字典，获取字典格式的返回值
assert r.json()["status"] == 200  #判断结果码是否正确

# 3.数据库校验
# (本次要查询所有的轮播图 id是否存在)
data = r.json()["data"]
for i in data:
    #  print(i["id"])
    # 每次循环之后，都会查询一下数据库
    sql = "select * from t_title_img where id = {}".format(i["id"])
    res = query(sql)
    # print(res)
    assert len(res) != 0
    print("id在数据库当中")


# 有参数的post接口
url = "http://118.24.105.78:2333/login"
data = {"username":"zhdch","password":"zhdch123"}
h = {"Content-Type":"application/json"}
res = requests.post(url=url,json=data,headers=h)
print(res.text)
assert res.status_code == 200
assert res.json()["status"] == 200
sql = "select * from t_user where username = 'zhdch'"
assert len(query(sql)) != 0
print("接口测试成功")

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









