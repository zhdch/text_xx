
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

if __name__ == "__main__":
    pass   
    ago = int(input("你的年龄是："))
    if ago > 18:
        print("成年人")
    elif ago > 14:
        print("青少年")
    elif ago > 6:
        print("儿童")
    else:
        print("婴儿")
