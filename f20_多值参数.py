# 可变参数  * 元组 args; ** 字典 kwargs
# def demo(num, *args, **kwargs):
#     print(num)  # 1
#     print(args)  # (2, 3, 4, 5)
#     print(kwargs)  # {'name': 'xiao', 'age': 18, 'gender': True}


# demo(1, 2, 3, 4, 5, name="xiao", age=18, gender=True)


# def sum_numbers(*args):
#     num = 0
#     for arg in args:
#         num += arg
#
#     return num
#
#
# print(sum_numbers(1, 2, 3, 4))

# 拆包
def demo(*args, **kwargs):
    print(args)  # (2, 3, 4, 5)
    print(kwargs)  # {'name': 'xiao', 'age': 18, 'gender': True}


g_args = (2, 3, 4, 5)
g_kwargs = {'name': 'xiao', 'age': 18, 'gender': True}
demo(*g_args, **g_kwargs)  # (2, 3, 4, 5) {'name': 'xiao', 'age': 18, 'gender': True}
demo(g_args, g_kwargs)  # ((2, 3, 4, 5), {'name': 'xiao', 'age': 18, 'gender': True}) {}
