class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    def eat(self):
        """重写（overwrite）"""
        print("Dog eat")

    def sleep(self):
        print("-----子类的开始-----")
        super().sleep()  # 等于 Animal().sleep() (不推荐)
        print("-----子类的结束-----")

    def bark(self):
        print("汪汪叫")


tom = Dog()
tom.eat()  # Dog eat
tom.bark()
tom.sleep()
