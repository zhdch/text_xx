a = 10
while a > 0:
    print(a)
    a = a - 1
# while遍历数值,通过 a = a - 1 从大到小遍历

# 红绿灯练习
a = 0
while a < 60:
    if a <= 5:
        print("红灯")
    elif a < 30:
        print("黄灯")
    else:
        print("绿灯")
    a = a + 1

# a = 0 是一个边界值，while 是在另外一个边界值的条件下遍历，其他条件在 while 里面进行，a = a + 1 在 while 处缩进


# 遍历元组/数组/字典
b = [2,7,16,14,9]
for i in b:
    if i > 10:
        print("真棒{}".format(i))
    else:
        print("继续努力{}".format(i))

# i 是作为一个变量按顺序依次取里面的值

#序列生成器
a = ["张三","李四","王五","路人甲","路人乙","路人丙","路人丁"]
for i in range(len(a)):
    print(a[i])  # 通过 i 遍历数组，通过下标打印元素

# 用 for 循环做的登陆校验
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

# 用 for 循环做的注册
b = [{"username":"小郭","password":"123456"},{"username":"小张","password":"123456"}]
u = input("请输入账号：")
p = input("请输入密码：")
c = 1
for i in b:
    if i.get("username") == u:
        print("账号已注册，请重新输入！")
        break
    elif len(b) == c:
        b.append({"username":u,"password":p})
        break
    c = c + 1
print(b)





