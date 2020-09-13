"""
# def 定义一个方法，目的是为了重复使用。
# 方法里面参数是可以有，也可以没有
def log():  # 通过定义，来实现调用方法
    print("哈哈哈")
log()
log() 

# 通过定义数学函数方法，是数学函数可以重复使用。
def s(x=2,y=3):   # 参数可以有默认值
    a = x * y
    return a
m = s(3,5)
n = s()
print(m)
print(n)
"""
"""
# 参数可以传任意的数据类型
# 通过定义登录方法，随意调用登陆方法
def login(u,p):
    t_user = [{"username":"小郭","password":"123456"},{"username":"小张","password":"123456"}]
    a = 1
    for i in t_user:
        print('这是第{}次运行，i的值是{}'.format(a,i))
        if i.get("username") == u and i.get("password") == p:
            print("登陆成功！")
            break
        elif len(t_user) == a:
            print("登陆失败，请重试") 
        a = a + 1
u = input("请输入账号：")
p = input("请输入密码：")
login(u,p)
"""
"""
# 注册的调用
def regist(u,p):
    b = [{"username":"小郭","password":"123456"},{"username":"小张","password":"123456"}]
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
u = input("请输入账号：")
p = input("请输入密码：")
regist(u,p)
"""

# 通过 Pymysql 第三方插件 ，调用方法连接数据库(这里运行一直报错，单独拉出去运行就 OK 了)
import pymysql  # 要想用Pymysql，就必须要导入它
def query(sql):
    # 固定的方法
    db = pymysql.connect(host='140.143.6.172', user='root', password='zhdch0708', db='zdc_study')
    # 获取查询窗口：游标
    cur = db.cursor()
    # 执行sql语句
    cur.execute(sql)
    # 获取所有的结果
    res = cur.fetchall()
    db.close()
    return res

# pymysql 查询数据库
if __name__ == "__main__":
    # sql = ("select * from report where id = 1")
    # a = query(sql)
    # print(a)

# pymysql 连接数据库登陆账号
    u = input("请输入账号：")
    p = input("请输入密码：")
    sql = ("select * from xinxi where username ='{}' and password ='{}'".format(u,p))
    res = query(sql)
    if len(res) != 0:
        print("登陆成功")
    else:
        print("登陆失败")

# pymysql 连接数据库查询数据
    sql = ("select sname,math from report")
    res = query(sql)
    for i in res:
        if i[0] == "景天":
            if i[1] > 90:
                print("{},真棒".format(i[0]))
            else:
                print("{},继续努力".format(i[0]))   


# 单独拉出来都成功了，在这死活运行不过去！！！！
