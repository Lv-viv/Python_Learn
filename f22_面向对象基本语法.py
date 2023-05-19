# dir内置函数 函数/标识符
# print(dir(print))


# 定义一个类
class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建对象
tom = Cat()
# 调用
tom.eat()
tom.drink()

print(tom)  # <__main__.Cat object at 0x0000025B9D878D90>
addr = id(tom)
print("%d" % addr)  # 2741852605584 ==> 0x0000025B9D878D90


lazy_cat = Cat()
print(lazy_cat)
lazy_cat2 = lazy_cat
print(lazy_cat2)


