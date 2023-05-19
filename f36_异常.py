# 简单的
# try:
#     # 不能确实正确执行的代码
#     a = int(input("输入整数: "))
# except:
#     print("error")
#
# print("-" * 25)

# 错误类型捕获
# try:
#     num = int(input("输入一个整数："))
#     # result = 8 / num
#     # print(result)
# # except ValueError:
# #     print("输入不是整数")
#
# except ZeroDivisionError:
#     print("输入为0")
#
# except Exception as result:
#     print("未知错误 %s" % result)


"""完整语法"""
# try:
#     pass
# except ZeroDivisionError:
#     pass
# except (ZeroDivisionError, ValueError):
#     pass
# except Exception as result:
#     pass
# else:
#     # 没有错误才执行
#     pass
# finally:
#      # 无论是否异常都执行
#     pass


"""指定义异常"""


def input_password():
    pwd = input("输入密码: ")
    if len(pwd) >= 8:
        return pwd
    print("抛出异常")
    ex = Exception("密码长度不够")
    raise ex


try:
    input_password()

except Exception as result:
    print(result)
