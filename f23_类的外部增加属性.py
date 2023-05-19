class Cat:

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("小猫要喝水")

tom = Cat()
lazy_cat = Cat()
# .属性名 利用赋值语句

tom.name = "Tom"
lazy_cat.name = "Lazy"
tom.eat()
# print(dir(tom))
# print(tom.name)
# print(lazy_cat.name)


