str1 = "Hello, World"
str2 = 'Hello, world'

for ch in str1:
    print(ch)

print(len(str1))

print(str1.count("Hello"))

print(str1[0])
print(str1.index("World"))
# print(str1.index("abc"))      # ValueError: substring not found

# 判断空白字符
space_str = "       \t\n\r"
print(space_str.isspace())

# 是否只有数字
# 不能判断小数
# num_str = "1"
# num_str = "(1)"
# num_str = "\u00b2"  # ²
# num_str = "一千"
# print(num_str)
# print(num_str.isdecimal())
# print(num_str.isdigit())
# print(num_str.isnumeric())

# #  查找
# hello_str = "hello world"
# # 开始
# print(hello_str.startswith("hello"))
#
# # 结尾
# print(hello_str.endswith("world"))
#
# # 查找指定字符串 不存在-1
# print(hello_str.find("world"))
#
# # 替换
# print(hello_str.replace("hello", "Hello"))  # Hello world
# print(hello_str)    # hello world


# 文本对齐
# poem = ["等和偶", "weang", "hjdaskhfkas", "jdkahasdi"]
# for poem_str in poem:
#     print(poem_str.center(10, '*'))  # 居中
#
# for poem_str in poem:
#     print(poem_str.ljust(10, "*"))  # 左对齐
#
# for poem_str in poem:
#     print(poem_str.rjust(10, "*"))  # 右对齐


# # 去除空白字符
# space_str = "  dasd   adasd  "
# print(space_str.strip())  # dasd   adasd

# # 拆分/拼接
# split_str = "hello,word"
# # 拆分
# temp_list = split_str.split(',')
# print(temp_list)  # ['hello', 'word']
# # 合并
# join_str = ",".join(temp_list)
# print(join_str)  # hello,word

# 切片
num_str = "0123456789"
print(num_str[2:6])  # 2345
print(num_str[2:])  # 23456789
print(num_str[:6])  # 012345
print(num_str[::2])  # 02468
print(num_str[-1])  # 9
print(num_str[-1::-1])  # 9876543210
