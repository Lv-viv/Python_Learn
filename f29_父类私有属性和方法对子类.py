class Base:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("this is test")

    def test(self):
        self.__test()
        print(self.__num2)


class Sun(Base):
    def dome(self):
        self.test()


b = Sun()
b.dome()
