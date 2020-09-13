"""
a = {"name":"张小凡","age":12} # {key:value}
print(a["name"])
print(a["age"])

# 字典没有下标的概念
# 说明了，字典没有顺序的说法
# 字典取值，靠key


# 取值
print a["name"]   # 当key不存在时，报错
a.get("name")    #当key不存在时，返回空
# 新增和修改
a["name"] = "成都"    # 当key不存在时，就会新增；当key存在时，就修改
a,update(address="王二")  # update的写法的时候，key在这里是一个变量的写法
print(a)
# 取走
a.pop("name")
# 通过字典的方法，可以删字典，可以删数组
del a["name"]
print(a)

"""

a = {"xm":"周鼎成","age":"29"}

# # 增加
# a ["sg"] = 170
# # 修改
# a ["sg"] = 172
# # 删除
# del a ["sg"] =172
# # 




"""
# python的语句
# if: 条件语句
a = 20

if a >=18:
    print("成年人，不能早睡")
else:
    print("未成年，可以早睡")

> <  ;  >=  ;  <=

# 字符串条件 in，判断某个字符串是否在另一个字符串中
t = "你俩还争风吃醋"
y = "争风吃醋"
if y in t：
    print("在")
else：
    print("不在")

b = 123
c = 123
if b != c:
    print("b=c")
else:
    print("b不等于c")

a = int(input("请输入:"))
if a > 18:
    print("黄花大闺女")
else:
    print("钢铁直男")

a = len(input("请输入:"))
if a > 6:
    print("飞机")
else:
    print("大炮")


# 多条件：长度为3个字，名字：金字塔
name = input("关押白素贞的地方:")
if name == "金字塔" and len(name) == 3:
    print("正确")
else:
    print("错误")

name = input("关押白素贞的地方:")
if name == "金字塔" or len(name) == 3:
    print("正确")
else:
    print("错误")


# 多条件if嵌套
name = input("关押白素贞的地方")
if name =="金字塔":
    if len(name) == 3:
        print("字数错误")
    else:
        print("正确")
else:
    print("答对了")

"""

# 多条件递推式判断elif
# a = int(input("请输入:"))
# if a > 18:
#     print("成年人")
# elif a > 16:
#     print("青年人")
# elif a > 14:
#     print("青少年")
# elif a > 10:
#     print("娃娃")
# elif a > 4:
#     print("小朋友")
# else:
#     print("婴儿")

"""
username = len(input("请输入:"))
password = int(input("请输入:"))
if username > 5 and username < 8:
    print("账号正确")
else:
    print("账号长度不正确，请输入长度大于5且小于8位数的字符")     
if password == 123456 and username > 5 and username < 8:
    print("登陆成功")
else:
    print("密码错误，登陆失败")

username = input("账号:")
password = int(input("密码:"))
if username == "张三123456" and password == 123456:
    print("登陆成功")
else:
    print("登陆失败")


a = float(input("请输入"))
b = float(input("请输入"))
print("结果:",a + b)
"""

# a = 10
# while a > 0:
#     print(a)
#     a = a - 1

# a = 0
# cj = [80,65,40,58,95]
# while a < 5:
#     if cj[a] < 60:
#         print("优秀，成绩是{}".format(cj[a]))
#     a = a + 1

# a = 60
# while a > 0:
#     if a > 25 and a < 60:
#         print("绿灯")
#     if a > 5 and a < 26:
#         print("红灯") 
#     if a < 6:
#         print("黄灯")
#     a = a - 1

# a = 0
# while a < 60:
#     if a < 6:
#         print("黄灯")
#     if a > 5 and a < 26:
#         print("红灯")
#     if a > 25 and a < 61:
#         print("绿灯")
#     a = a + 1


# # 遍历元组/数组
# cj = [80,60,42,58,87]
# for a in cj:
#     print(a)
#     if a > 60:
#         print("真棒")

"""
#遍历字典
account = {"张三":"男生","李四":"女生"}
for a in account:
    print(a)
    print(account[a])

# 补充
for a in account.keys():
    print(keys)
for a in account.values():
    print(values)
for a in account.items():
    print(keys)
    print(values)
"""

# #序列生成器
# a = ["张三","李四","王五","路人甲","路人乙","路人丙","路人丁"]
# for i in range(len(a)):
#     print(a[i])
"""
a = [[1,2,3],[4,5,6]]
b = [{"username":"小郭","password":"123456"},{"username":"小张","password":"123456"}]
# for i in a:
#     for j in i:
#         print(j)
for i in b:
    for j in i:
        print(j)
        print(i[j])
"""
"""
t_user = [{"username":"小郭","password":"123456"},{"username":"小张","password":"123456"}]
u = input("请输入账号：")
p = input("请输入密码：")
a = 1
for i in t_user:
    if i.get("username") == u and i.get("password") == p:
        print("登陆成功！")
        break
    elif len(t_user) == a:
        print("登陆失败，请重试") 
    a = a + 1
"""
"""
b = [{"username":"小郭","password":"123456"},{"username":"小张","password":"123456"}]
u = input("请输入账号：")
p = input("请输入密码：")
c = 1
for i in b:
    if i.get("username") == u:
        print("账号已注册，请重新输入！")
        break
    elif len(b) == c:
        d = {}
        d["username"] = u
        d["password"] = p
        b.append(d)
        break
    c = c + 1
print(b)
"""
# def jia(x,y):
#     sum = x + y
#     return sum
# a = jia (3,6)
# print(a)

"""
def regist(u,p):
    b = [{"username":"小郭","password":"123456"},{"username":"小张","password":"123456"}]
    c = 1
    for i in b:
        if i.get("username") == u:
            print("账号已注册，请重新输入！")
            break
        elif len(b) == c:
            d = {}
            d["username"] = u
            d["password"] = p
            b.append(d)
            break
        c = c + 1
    print(b)
u = input("请输入账号：")
p = input("请输入密码：")
regist(u,p)
 
"""
"""
import pymysql
# 准备访问数据库
def query(sql):
    # 固定的方法
    db = pymysql.connect(host='140.143.6.172', user='root', password="zhdch0708", db='zdc_study')
    # 获取到查询窗口：游标
    cur = db.cursor()
    # 执行sql语句
    cur.execute(sql)
    # 获取所有的结果
    res = cur.fetchall()
    db.close()
    return res
a = query("select * from report where id = 5")
print(a)
# 通过python来查询数据库的表内容

#结合数据库查询账号密码
u = input("请输入账号：")
p = input("请输入密码：")
sql = "select * from t_user where username='{}' and password='{}'".format(u,p)
res = query(sql)
if len(res) != 0: #数据库中查询到了结果，账号和密码匹配
    print("登陆成功！")
else:
    print("登陆失败！")
"""
a = [1,3,4]
try:
    res = a[10]
    print("好好干")
except:
    print("就会有好结果")