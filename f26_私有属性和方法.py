class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18  # 私有属性

    def __secret(self):
        # 私有方法，对象内部可以访问
        print("%s的年龄是%d" % (self.name, self.__age))


xiaofang = Women("小芳")

# 伪私有
print(xiaofang._Women__age)  # 18
xiaofang._Women__secret()  # 小芳的年龄是18
