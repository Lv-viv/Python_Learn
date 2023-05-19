# 不可变参和可变参
# def demo(num, num_list):
#     num = 100  # 100
#     num_list = [3, 2, 1]
#     print(num)
#     print(num_list)  # [3, 2, 1]
#
#
# g_num = 1
# g_list = [1, 2, 3]
# demo(g_num, g_list)
# print(g_num)  # 100
# print(g_list)  # [1, 2, 3]


# 可变

# def demo(num_list):
#     num_list.append(9)
#     print(num_list)  # [3, 2, 1]
#
#
# gl_list = [1, 2, 3]
# demo(gl_list)
# print(gl_list)  # [3, 2, 1]


def demo(num, num_list):
    """ 对列表 += 本质为extend """
    num += num
    num_list += num_list
    # num_list = num_list + num_list 不会影响外部实参
    print(num)      # 18
    print(num_list)  # [1, 2, 3, 1, 2, 3]


gl_num = 9
gl_list = [1, 2, 3]
demo(gl_num, gl_list)
print(gl_num)  # 9
print(gl_list)  # [1, 2, 3, 1, 2, 3]
