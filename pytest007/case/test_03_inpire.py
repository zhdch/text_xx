import pytest
import requests
# 表兄弟关系跨文件夹导入包，一定是sys在前，from在后
import os, sys
sys.path.append(os.getcwd())  
from utils.dbtools import query
from utils.filetools import save_file,read_file

def test_01_fblg():
    # 构造请求
    url = 'http://118.24.105.78:2333/inspirer/new'
    data = {"content":"内ssss容","ximg":"dsfsdf.jpg"}
    h1 = {"Content-Type":"application/json", "token":read_file()}
    res = requests.post(url=url, json=data, headers=h1)
    print(res.text)
    # 断言
    assert res.status_code == 200
    assert res.json()['status'] == 200
    
    # 数据库查询
    inspirerid = res.json()['data']['inspirerid']
    sql = "select * from t_inspirer where id={}".format(inspirerid)
    assert len(query(sql)) == 1
    # save_filee(inspirerid)


    

    
