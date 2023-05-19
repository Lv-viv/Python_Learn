# 定义类方法
class Tool:
    count = 0

    @classmethod
    def show_tool_count(cls):
        """显示工具对象个数"""
        print("当前有%d个工具" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("锤子")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

Tool.show_tool_count()