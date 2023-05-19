# 用元组返回多个结果
def measure():
    return 39, 24


result = measure()  # 元组类型
print(result)  # (39, 24)

# 单独处理温度和湿度 - 不方便
print(result[0])
print(result[1])

# 如果是元组，切单独处理元素
gl_temp, gl_wetness = measure()

print(gl_temp)  # 39
print(gl_wetness)  # 24

# 交换
a = 1
b = 2
a, b = b, a
print(a)  # 2
print(b)  # 1


