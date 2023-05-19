class Dog(object):
    # 定义一个静态方法
    @staticmethod
    def run():
        # 不访问实例属性，类属性
        print("小狗要跑")


# 调用
Dog.run()
