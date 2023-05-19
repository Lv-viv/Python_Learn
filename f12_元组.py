info_tuple = ("zhangsan", 18, 1.75)
print(info_tuple[1])  # 18
empty_tuple = ()
one_tuple = (19,)  # 一个元素要有,
signal_tuple = (19)  # int类型

info_tuple.index(18)

for info in info_tuple:
    print(info)
"""
zhangsan
18
1.75
"""
# 应用：函数参数，返回值；格式化字符串，让列表数据不被修改
print("%s的年龄 %d 身高为 %.2fm" % info_tuple)  # zhangsan的年龄 18 身高为 1.75m
print("%s的年龄 %d 身高为 %.2fm" % ("zhangsan", 18, 1.75))
info_str = "%s的年龄 %d 身高为 %.2fm" % info_tuple
print(info_str)  # zhangsan的年龄 18 身高为 1.75m

# 元组和列表转换
num_list = [1, 2, 3, 4]
num_tuple = tuple(num_list)
num_list = list(num_tuple)

print(type(num_list))
print(type(num_tuple))