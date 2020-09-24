# """a = int(input("请输入:"))
# if a > 18:
#     print("黄花大闺女")
# else:
#     print("钢铁直男")

# a = len(input("请输入:"))
# if a > 6:
#     print("飞机")
# else:
#     print("大炮")

# name = input("关押白素贞的地方:")
# if name == "金字塔" and len(name) == 3:
#     print("正确")
# else:
#     print("错误")

# name = input("关押白素贞的地方:")
# if name == "金字塔" or len(name) == 3:
#     print("正确")
# else:
#     print("错误")

# name = input("关押白素贞的地方")
# if name =="金字塔":
#     if len(name) == 3:
#         print("字数错误")
#     else:
#         print("正确")
# else:
#     print("答对了")
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
"""

# a = float(input("请输入"))
# b = float(input("请输入"))
# print("结果:",a + b)

"""
a = int(input("请输入数字"))
if a % 2 == 1 and a > 0:
    print("单数")
elif a > 0:
    print("双数")
elif a <= 0:
    print("无效数字")
"""
"""
a = len(input("请输入"))
if a % 2 == 0:
    print("偶数")
if a % 2 == 1:
    print("奇数")
"""

# b = ("学习","开学",6,8)
# a = (1,3,4,"学习","放假",b)
# print(a[-1][0])
"""
a = int(input("请输入数字"))
if a % 2 == 1 and a > 0:
    print("单数")
elif a > 0:
    print("双数")
elif a <= 0:
    print("无效数字")

username = input("账号:")
password = int(input("密码:"))
if username == "张三123456" and password == 123456:
    print("登陆成功")
else:
    print("登陆失败")
"""

# a = 10
# while a > 0:
#     print(a)
#     a = a - 1


# a = 0
# cj = [80,65,40,58,95]
# while a < len(cj):
#     if cj[a] < 60:
#         print("继续努力，成绩是{}".format(cj[a]))
#     a = a + 1

"""
cj = [86,35,77,68,61,49,58]
good = []
bad = []
for i in cj:
    if i > 60:
        good.append(i)
    else:
        bad.append(i)
print(good)
print(bad)
"""
# account = {"username":"小明","成绩":"88"}
# for i in account:
#     print(i)
#     print(account.get(i))

"""
account = {"username":"小明","成绩":"92"}
for i in account.keys():
    print(i)
for i in account.values():
    print(i)
"""
"""
aaa = "今天的风好大，天气变冷了，该添衣裳了。"
for i in aaa:
    print(i)

for i in range(10):
    print(i)

a = ("景天","徐长卿","龙葵","雪见","茂茂","小土豆","重楼","火鬼王","重楼")
for i in range(len(a)):
    print(a[i])

def jianfa(s1=10,s2=3):
    sa = s1 * s2
    return sa
a = jianfa(9,6)
b = jianfa()
print(a)
print(b)
"""
a = {"一班":"文科","二班":"理科","三班":"文科"}
print(a["二班"])