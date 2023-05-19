#
num_str = [1, 2, 3, 4]
print(len(num_str))
del (num_str[1])
print(num_str)
key_val = {"a": "z", "b": "c"}
print(max(key_val))
print(min(key_val))
# cmp(item1,item2) 在python3.0删除
# 字典不能比较大小
isEmpty = "AAA" < "BBB"
print(isEmpty)

#
print([0, 1, 2, 3, 4][1:3])  # [1, 2]
print([0, 1, 2, 3, 4][1:3:2])  # [1]
print([0, 1, 2, 3, 4][1:3:1])  # [1, 2]
print([0, 1, 2, 3, 4][1:3:4])  # [1]

#
{}.copy()
print([1, 2] * 5)  # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print([1] + [2])  # [1, 2]
print("a" in {"a": "a"})  # True
print("b" not in {"a": "a"})  # True

t_list = [1, 2, 3, 4]

t_list.append(0)
print(t_list)
t_list.append([7, 8])
print(t_list)  # [1, 2, 3, 4, 0, [7, 8]]

for a in [1,  2, 4, 5]:
    print(a, end="")
else:
    print("成功")
# 1245成功

for a in [1, 2, 3, 4, 5]:
    print(a, end="")
    if a == 3:
        break
else:
    print("成功")
# 123

find_name = "atu"
students = [{"name": "atu"}, {"name": "xiaomei"}]
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        break
else:
    print("没找到")