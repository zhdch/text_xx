# 通过 Pymysql 第三方插件 ，调用方法连接数据库(这里运行一直报错，单独拉出去运行就 OK 了)
import pymysql # 要想用pymysql，就必须要导入它
def query(sql):
    # 固定的方法
    db = pymysql.connect(host='118.24.105.78', user='root', password="1qaz!QAZ123***123", db='ljtestdb')
    # 获取查询窗口：游标
    cur = db.cursor()
    # 执行sql语句
    cur.execute(sql)
    # 获取所有的结果
    res = cur.fetchall()
    db.close()
    return res

if __name__ == "__main__":
    a = query("select * from t_user where id = 1111")
    print(a)
