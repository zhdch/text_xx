# 这个文件下面存放所有的首页相关的测试用例
# 必须要在 pytest007文件夹下用 cmd终端运行 pytest

import pytest
import requests
import os, sys
sys.path.append(os.getcwd()) 
from utils.xlrdtools import read_excel

def test_01_lbt():
    data_res = read_excel("data\测谈网测试用例.xlsx", "首页")
    # 这里面就写 requests的代码
    url = data_res[0][2]
    res = requests.get(url)
    assert res.status_code == 200
    assert res.json()['status'] == 200

def test_02_tjjc():
    data_res = read_excel("data\测谈网测试用例.xlsx", "首页")
    url1 = data_res[1][2]
    res1 = requests.get(url=url1)
    # print(res1.text)
    assert res1.status_code == 200
    assert res1.json()['status'] == 200
