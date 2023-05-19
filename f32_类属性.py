# 类是一个特殊的对象

class AAA:
    pass


# 类名.属性
print(AAA.__init__)  # <slot wrapper '__init__' of 'object' objects>

# 类名.方法
print(AAA.__str__(AAA))  # <class '__main__.AAA'>


# 自定义类属性
class Tools:
    # 赋值语句创建,类属性
    count = 0

    def __init__(self, name):
        self.name = name
        Tools.count += 1


tool1 = Tools("锤子")
print(Tools.count)
print(tool1.count)  # 不推荐

tool2 = Tools("榔头")
tool3 = Tools("水桶")

tool3.count = 99        # 生成实例属性
print(tool2.count)
print(tool3.count)
