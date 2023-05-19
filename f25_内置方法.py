class Cat:

    def __init__(self, name):
        print("这是一个初始化方法")
        self.name = name

    def __del__(self):
        print("__del__")

    def __str__(self):
        """
        必须返回字符串
        """
        return "我是小猫%s" % self.name

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("小猫要喝水")



tom = Cat("Tom")
print(tom.__str__())  # 我是小猫Tom; 默认:<__main__.Cat object at 0x000001B8A4C89410>
