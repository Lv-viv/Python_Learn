name_list = ["张三", "李四", "王五"]
# 1 取值和去索引
print(name_list[0])  # 张三

# list index out of range
# print(name_list[3])

print(name_list.index("张三"))  # 0
# print(name_list.index("张三123"))     # '张三123' is not in list

# 2 修改
name_list[0] = "lisi"
print(name_list[0])

# 3 增加
print(name_list)  # ['lisi', '李四', '王五']
name_list.insert(1, "王小二")
print(name_list)  # ['lisi', '王小二', '李四', '王五']
name_list.append("哇哈哈")
print(name_list)  # ['lisi', '王小二', '李四', '王五', '哇哈哈']
temp_list = ["孙悟空"]
name_list.extend(temp_list)
print(name_list)  # ['lisi', '王小二', '李四', '王五', '哇哈哈', '孙悟空']

# 4 删除
name_list.pop()
print(name_list)  # ['lisi', '王小二', '李四', '王五', '哇哈哈']
name_list.pop(2)
print(name_list)  # ['lisi', '王小二', '王五', '哇哈哈']
name_list.remove("lisi")
print(name_list)  # ['王小二', '王五', '哇哈哈']
# name_list.clear()
# print(name_list)        # []
# del 本质是从内存中删除
del name_list[1]
print(name_list)  # ['王小二', '哇哈哈']

# 统计
# print(len(name_list))   # 2
# count_list = [1, 1, 1, 2]
# print(count_list.count(1))   # 3

# 排序，反转
name_list.sort()  # 升序
print(name_list)  # ['哇哈哈', '王小二']
name_list.sort(reverse=True)    # 降序
print(name_list)  # ['王小二', '哇哈哈']
name_list.reverse()     # 反转
print(name_list)  # ['哇哈哈', '王小二']

#      for循环
"""
哇哈哈
王小二
"""
for name in name_list:
    print(name)
