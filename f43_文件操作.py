# file = open("test.txt", "r", encoding='utf-8')
# # text = file.read()
# # print(text)
# # print(len(text))
#
# # text = file.read()
# # print(len(text))
# while True:
#     text = file.readline()
#     if not text:
#         break
#     print(text)
#
# file.close()


# 文件和目录管理
import os
# os.rename("test.txt", "remove_test.txt")
print(os.listdir(os.getcwd()))
print(os.getcwd())

