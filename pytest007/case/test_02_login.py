import pytest
import requests
# 表兄弟关系跨文件夹导入包，一定是sys在前，from在后
import os, sys
sys.path.append(os.getcwd())  
from utils.dbtools import query  # 直接调 pymysql连接数据库的方法
from utils.xlrdtools import read_excel
from utils.filetools import save_file

def test_02_login_sussess():
    # 登陆成功的测试用例
    data_res = read_excel("data\测谈网测试用例.xlsx", "登陆")

    url = data_res[0][2]         # 根据excel直接读取
    data = eval(data_res[0][4])     # eval是读取字典内容
    header = eval(data_res[0][5])
    res = requests.post(url=url, json=data, headers=header)
    print(res.text)
    
    # 状态码和结果码成功的断言
    assert res.status_code == 200
    assert res.json()['status'] == int(data_res[0][6])

    # 数据库的校验
    sql =  "select * from t_user where username = '{}'".format(data["username"])
    assert len(query(sql)) != 0

    # 保存最后一次登陆的 token值
    token = res.json()["data"]["token"]
    save_file(token=token)

def test_02_login_fail():
    # 四位数账号登陆失败
    data_res = read_excel("data\测谈网测试用例.xlsx", "登陆")

    url = data_res[1][2]
    data = eval(data_res[1][4])
    header = eval(data_res[1][5])
    res = requests.post(url=url, json=data, headers=header)
    print(res.text)
    # 状态码和结果码成功的断言
    assert res.status_code == 200
    assert res.json()['status'] == int(data_res[1][6])