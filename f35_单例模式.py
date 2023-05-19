# class MusicPlayer:
#     def __init__(self):
#         print("播放器初始化")
#
#     def __new__(cls, *args, **kwargs):
#         # 1. 创建对象是new会被自动调用
#         print("创建对象，分配空间")
#         # 2. 为对象分配空间
#         instance = super().__new__(cls)
#         # 3. 返回对象引用
#         return instance
#
#
# player1 = MusicPlayer()
# print(player1)  # <__main__.MusicPlayer object at 0x000002121ADE8D90>
# player2 = MusicPlayer()
# print(player2)  # <__main__.MusicPlayer object at 0x000002121ADE8DD0>


# 单例模式 但__init__还好多次调用
# class MusicPlayer:
#     instance = None
#
#     def __init__(self):
#         print("播放器初始化")
#
#     def __new__(cls, *args, **kwargs):
#         # 1. 创建对象是new会被自动调用
#         print("创建对象，分配空间")
#         # 2. 为对象分配空间
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#         # 3. 返回对象引用
#         return cls.instance
#
#
# player1 = MusicPlayer()
# print(player1)  # <__main__.MusicPlayer object at 0x0000026C637C8C90>
# player2 = MusicPlayer()
# print(player2)  # <__main__.MusicPlayer object at 0x0000026C637C8C90>


class MusicPlayer:
    instance = None
    init_flag = False

    def __init__(self):
        if MusicPlayer.init_flag is False:
            # 初始化动作
            print("播放器初始化")
            MusicPlayer.init_flag = True

    def __new__(cls, *args, **kwargs):
        # 1. 创建对象是new会被自动调用
        # print("创建对象，分配空间")
        # 2. 为对象分配空间
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        # 3. 返回对象引用
        return cls.instance


player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
# 播放器初始化
# <__main__.MusicPlayer object at 0x0000022FCF3E8D50>
# <__main__.MusicPlayer object at 0x0000022FCF3E8D50>
