from f38_测试模块1 import Dog
# from f38_测试模块1 import * 导入所有工具
from f38_测试模块1 import say_hello
from f39_测试模块2 import say_hello

say_hello()  # 后导入覆盖
dog = Dog()
print(dog)

