# a = 1
# print(id(a))  # 140705890886440
# print(id(1))  # 140705890886440
# b = a
# print(id(b))  # 140705890886440


# def test(num):
#     print(id(num))  # 140705890886728
#     pass
#
#
# a = 10
# print(id(a))  # 140705890886728
# test(a)
#
#
# def test1():
#     b = 10
#     print(id(b))    # 140705890886728
#     return b
#
#
# a = test1()
# print(id(a))    # 140705890886728


# 可变、不可变类型
# a = 1
# a = "hello"
# a = [1, 2, 3]
# a = [3, 2, 1]

# 全局变量不能使用 赋值 改变
# num = 10
# def g_fun1():
#     num = 1     # 局部变量
#     print(num)  # 1
#
#
# def g_fun2():
#     print(num)  # 10
#
#
# g_fun1()
# g_fun2()


# global 修改全局变量
num = 10


def g_fun1():
    global num  # 全局变量
    num = 1
    print(num)  # 1


def g_fun2():
    print(num)  # 1


g_fun1()
g_fun2()
