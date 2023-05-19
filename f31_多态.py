class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 玩耍" % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s 飞贷玩耍" % self.name)


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 玩耍。。。" % (self.name, dog.name))
        dog.game()


# 创建dog对象
wangcai = Dog("旺财")
xiaotianquan = XiaoTianDog("旺财")

xiaoming = Person("小明")
# 多态
xiaoming.game_with_dog(xiaotianquan)
