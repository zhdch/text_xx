# a = 1
# b = []
# while a <= 1000:
#     if a % 2 == 0:
#         b.append(a)
#     a = a + 1
# print(len(b))

# a = [22,33,1,4,5,6,7]
# for i in a:
#     for j in i:

# a = int(input("请输入数字："))
# b = []
# for i in range(a):
#     if a % (i+1) == 0:
#         b.append(i+1)
# print(b)

# a = {"username":"乔美丽","username":"王美丽","username":"郭然然","username":"周美丽"}
# for i in a:
#     if "美丽" in a:
#         print(a)
# a = int(input("请输入第一个数字："))
# b = int(input("请输入第二个数字："))
# print("它们的和等于",a+b)
a = 1
b = []
while a <=1000:
    if a % 2 ==0:
        b.append(a)
    a = a + 1
print(len(b))

a = [2,1,13,5,37,9]
n = len(a)-1
while n > 0:
    for i in range(n):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    n = n + 1
    print(a)
    break

a = [3,9,8]
a[1],a[2]=a[2],a[1]   # 通过定义赋值，将位置调换了
print(a)

# 输入一个数字，判断 4 2 5/2 10 的因数有哪些？
a = int(input("数字："))
b = []
for i in range(a):
    if a % (i+1) == 0:
        b.append(i+1)
print(b)


a = {"username":"乔美丽","username1":"郭然然","username2":"周美丽","username3":"王美丽"}
b = []
c = "美"
print(a.values())
for i in a.values():
    if c in i:
        b.append(i)
print(b)


