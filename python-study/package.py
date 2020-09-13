# 导入包 : import 包名
import time
time.sleep(5)  # 延迟包
print("哈哈哈")
# unittext包   自动化测试框架
# math包
import math
a = math.sqrt(4) # 根号
print(a)
# random包  产生随机数
import random
print(random.randint(1,20))

# 第三方包
# 通过管理员身份运行cmd，用python的pip工具安装的 (pip,pip3)
#1.pip -V       (查看pip版本号)
#2.pip list      (查看已安装的第三方包)
#3.pip install 包名     (安装第三方包) 管理员身份运行cmd来安装
#4.pip install requests -i 下载地址   (一般都是通过地址下载第三方包的)
#5.pip uninstall 包名     (卸载第三方包)
#  主要的第三方包:
# selenium : web自动化测试
# request : 是用python做http请求的，主要做接口自动化测试， 爬虫等
# pymysql : 连数据库的包 (连接数据库是为了做接口自动化最后一步) 


# 导入自定义包
#1.创建包：新建一个自定义文件夹，文件夹下边新建一个__init__.py，再把 方法/变量/类的py文件放入文件夹中
#2.from 包名.py文件名 import 方法/变量/类
#3.from 文件名 import 方法/变量/类

from backage.fangfa import t_user 
print()

# if __name__ == "__main__":  # 一般用 if main 来停止导入过程中的运行
#   pass   



# 定位报错 /异常处理
# 找到文件名称，可以看到报错的行，或者 ctrl鼠标左键单击报错的句子，光标就会指到报错的行。

# 试着运行 try里面的代码，如果正确，就运行 try后面的代码，不运行 except后面的；如果有出错的，则不能运行 try后面的，只能运行 except后面的
a = (1,3,8,5)
try:     
    a[5]
    print("good morning")
except Exception as e:   # exception as e 找出报错原因， print(e)就能打印报错原因
    print(e)
    print("hello world")

a = (1,3,8,5)
try:     
    a[1]       # try后面没报错，运行 try后面的
    print("没错")
except:
    print("错了")    # 报错了，运行 except后面的
else:
    print("真的没错")     # 没有报错的情况
finally:
    print("对错都有我")     # 报不报错都运行







