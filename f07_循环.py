#   while循环
# number = 0
# while number < 10:
#     if number == 2:
#         number += 1
#         continue
#     elif number == 9:
#         break
#     print(number)
#     number += 1
# 循环嵌套
# i = 0
# while i < 10:
#     print("条件1： %d" % i)
#     if i == 5:
#         while i < 8:
#             print("条件2：%d" % i)
#             i += 1
#     i += 1

i = 0

while i < 5:
    j = 0
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1
# print的结尾处理
# print("*", end="")      # 不换行

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d * %d = %d " % (i, j, i * j), end="")
        j += 1
    print()
    i += 1
""" 
=,  +=,   -=,    *=, /=,  //=,  %=
"""