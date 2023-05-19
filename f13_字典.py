xiaoming = {"name": "小明", "age": 18, "gender": True, "height": 1.75}

print(xiaoming)  # {'name': '小明', 'age': 18, 'gender': True, 'height': 1.75}

#   取值
print(xiaoming["name"])
print(xiaoming.get("name"))
# 增加/修改
xiaoming["weight"] = 75
xiaoming["name"] = "小小民"
print(xiaoming)
# 删除
xiaoming.pop("weight")
# 随机删除
# xiaoming.popitem()
print(xiaoming)

# 统计键值对的数量
print(len(xiaoming))

# 合并字典
temp_dict = {"height": 1.75, "weight": 75}
xiaoming.update(temp_dict)
print(xiaoming)  # {'name': '小小民', 'age': 18, 'gender': True, 'height': 1.75, 'weight': 75}

# 清空
xiaoming.clear()
print(xiaoming)

# 循环遍历
xiaoming_dict = {"name": "小明", "qq": "123456", "phone": "123466799"}
for key in xiaoming_dict:
    print("%s: %s" % (key, xiaoming_dict[key]))
"""
name: 小明
qq: 123456
phone: 123466799
"""
print("*" * 50)
card_list = [{"name": "小明", "qq": "123456", "phone": "123466799"},
             {"name": "李四", "qq": "123456", "phone": "123466799"}]
for card_info in card_list:
    for info in card_info:
        print("%s->%s" % (info, card_info[info]))
    print("-" * 10)
