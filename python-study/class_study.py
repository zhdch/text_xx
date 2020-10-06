class Person():
    # 属性: 类的成员变量 (实例变量)
    mz = "周鼎成"
    nl = 18
    sex = "男"
    yanzhi = "超帅"
    # 命名规则 :驼峰命名 PersonText
    # 功能 :成员方法 (self为类本身，self不用传参)
    def fly(self):
        print("起飞了")
        return 233
    def eat(self,food):
        self.yanzhi = "极差"   # 调用类 :如果没有成员，就新增；如果有成员，就修改。
        self.fly()
        print("{},真能吃".format(self.mz,food))   # 通过 self.mz调成员，如果没有调用，就打印'海鲜'
# 实例化 :创建类的对象 :Person():把柄
p = Person()
print(p.mz)
print(p.nl)
p.fly()
print(p.fly())     # 成员方法的self不能传参
p.eat("海鲜")     #  format ()如果只有方法参数，可以打印新增(),如果有 self.成员，n那么就打印成员赋值。
print(p.yanzhi)

class BaBa():
    money = "1E"
    def make_money(self):
        print("他爸有个小目标")

# 类的继承，Son:子类   baba:父类
# 继承的好处：子类可以继承父类的属性和方法
# 子类可以重写父类的属性和方法

class Son(BaBa):
    name = "wsc"
    money = "-10E"
    def make_money(self):
        print("王同学不要小目标了")
        return 886

b = BaBa()
s = Son()
print(s.money)
print(b.money)
s.make_money()


class Cat():
    # 构造方法 :固定方法，类实例化的时候运行
    def __init__(self,mz,nl):
        self.name = mz
        self.age = nl
    def aa(self):
        a = 1      # 只针对aa有效
        self.b = 2      # 整个类都有效
# 一定要加参数
c = Cat("tomcat", 29)
print(c.name)
c.aa()
print(c.b)

# session cookies token (解决http无状态的bug)
# session：存在服务器端的用户标识
# cookie：存在客户端（浏览器）中的用户标识 (cookies劫持 :cookies本身是不安全的)
# token: 每次登陆的时候，前后端相保持登陆状态而产生的一个动态码     
# token一般是为了处理前后端分离产生的跨域问题 (保存用户登录的状态)

# 用 requests可以代替 postman调接口

