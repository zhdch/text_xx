# 框架 ：根据文件用途的不同，把对应的文件放到不同的文件夹下面

# pytext
# 一.简介 
# python自动化测试框架，第三方包
# 自动化测试，单元测试

# 二.作用
# 1.组织测试用例 :用方法来管理测试用例，一个方法就是一个测试用例
# 2.生成测试报告

# 三.环境
# pip install pytest -i https://pypi.tuna.tsinghua.edu.cn/simple

# 新建 pytest001文件夹，在 pytest文件夹下运行并新建四个文件夹
# case :存放测试用例的 
# conf :存放配置文件
# data :存放测试数据
# utils :存放工具代码

# 四.框架
# 分层
# 测试用例的划分 :
# 按模块名划分 :test_数字_模块名.py
# 普通方法 :test_数字_方法的名字.py

# 五.运行
# 切换到 pytest007文件夹下，用新终端运行 pytest
# pytest -s 显示 print的内容

# 六.结果
#   .代表成功   f带代表失败，或者代码报错

# 七.查找错误
# 1.找出报错的代码
# 2.打印出错的原因  (在断言assert之前 print，pytest -s)

# 八.关联
# 接口之间的依赖，上个接口的返回值，作为下个接口的参数
# 1.在登陆成功之后使用文件读写方法保存 token值
# 2.在要用的地方使用 read方法将 token读出来

# 九.测试用例设计
# 正向场景
# 逆向场景 :账号长度(四位数，五位数，十二位数，十三位数)
#          账号内容(特殊符号，重复账号)
#          密码长度(密码太长，密码太短)
#          密码内容(特殊符号，简易密码)
# 时间充足，正向逆向场景全覆盖
# 时间紧张，先测试正向场景
# 自动化测试用例最好的分类：一个sheet对应对应一个页面的接口 (这样接口不容易漏掉)

# 测试报告
# 1.jdk :先设置JAVA_HOME环境变量(里面填jdk的路径(在cmd中运行where java能看到))  # 上下都添加
#  CLASSPATH环境变量里面和在path里面添加 ;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;  # 上下都添加
# 2.安装allure-commandline(1.解压到指定文件夹  2.把 allure的bin路径复制粘贴到path变量中去)
# 3.安装allure-pytest第三方包 (pip3 install allure-pytest -i https://pypi.tuna.tsinghua.edu.cn/simple)
# 4.以管理员身份运行重启vscode， 在框架文件夹下，下边cmd终端运行:pytest --alluredir=result
# 5.把编译的结果翻译成报告:allure generate result -o report --clean 
# 6.打开测试报告 allure open -h 127.0.0.1 -p 10086 report
# **所有的case 都写完了，再去做测试 报告的生成
