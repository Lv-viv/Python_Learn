class A:
    def test(self):
        print("test 方法")

    def demo(self):
        print("A dome方法")


class B:
    def demo(self):
        print("demo 方法")


class C(A, B):
    pass


c = C()
c.test()
c.demo()
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
