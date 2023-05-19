# class Cat:
#
#     def eat(self):
#         print("%s爱吃鱼" % self.name)
#
#     def drink(self):
#         print("小猫要喝水")
#
#
# tom = Cat()

# 隐患
# tom.eat()  # 'Cat' object has no attribute 'name'
# tom.name = "Tom"


# 初始化方法
class Cat:
    def __init__(self, name):
        print("这是一个初始化方法")
        self.name = name

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("小猫要喝水")


tom = Cat("Tom")
tom.eat()