"""
当前版本为1.3

本版本主要更新内容：
加入活力值设定
"""
# 导入random、threading、time和tqdm库中的部分函数和类
# tqdm库是第三方库，需要先在命令提示符里用pip来下载
from random import randint
from threading import Thread
from time import sleep
from tqdm import trange


# 定义Person类，来模拟一个人
class Person:
    # 定义Person类的__init__()方法，也就是Person类的构造方法
    def __init__(self, name, sex, height, weight):
        self.name = name
        self.sex = sex
        self.height = height
        self.weight = weight
        self.age = 0
        self.heart = 3
        self.mood_index = 0
        self.vitality = 100
        self.alive = True
        print("这个人叫做", self.name, "，性别是", self.sex, "，身高和体重分别是", self.height, "厘米和", self.weight, "千克。")

    # 定义Person类的eat()方法，作用是让模拟人吃东西
    def eat(self, time):
        print(self.name, "饿了，请您给", self.name, "一些食物吧！")
        if input("请输入eat：") == "eat":
            food = input("请输入你要给的食物：")
            if food == "":
                self.heart -= 1
                print("失败！", self.name, "还剩", self.heart, "颗心。")
                # 判断还有没有心
                if self.heart == 0:
                    self.alive = False
                    print(self.name, "没有心了。抱歉，游戏结束。")
                    sleep(3)
                    exit()
            else:
                print("成功！请等待", time, "秒。")
                # 显示一个进度条
                for _ in trange(time):
                    sleep(1)
                    pass
                # 判断给模拟人的食物
                if food == "鸡肉" or food == "牛肉" or food == "鹅肉" or food == "芹菜":
                    self.mood_index += 10
                    if self.vitality < 100:
                        self.vitality += 10
                        if self.vitality >= 100:
                            self.vitality = 100
                    print(self.name, "很喜欢", food, "，心情指数加10。目前心情值为", self.mood_index, "，活力值为", self.vitality, "，谢谢您给", self.name, "食物。")
                elif food == "莲藕" or food == "菠菜" or food == "土豆":
                    self.mood_index += 5
                    if self.vitality < 100:
                        self.vitality += 10
                        if self.vitality >= 100:
                            self.vitality = 100
                    print(self.name, "喜欢", food, "心情指数加5。目前心情值为", self.mood_index, "，活力值为", self.vitality, "，谢谢您给", self.name, "食物。")
                else:
                    self.mood_index += 3
                    if self.vitality < 100:
                        self.vitality += 10
                        if self.vitality >= 100:
                            self.vitality = 100
                    print(self.name, "吃饱了，心情值加3。目前心情值为", self.mood_index, "，活力值为", self.vitality, "，谢谢您给", self.name, "食物。")
        else:
            self.heart -= 1
            self.vitality -= 5
            print("失败！", self.name, "还剩", self.heart, "颗心。")
            # 判断还有没有心
            if self.check_heart():
                self.die("模拟人没有心了")

    # 定义Person类的drink()方法，作用是让模拟人喝水
    def drink(self, time):
        print(self.name, "渴了，请您给", self.name, "一杯水吧！")
        if input("请输入drink：") == "drink":
            print("成功！请等待", time, "秒。")
            # 显示一个进度条
            for _ in trange(time):
                sleep(1)
                pass
            self.mood_index += 1
            print(self.name, "喝饱了，心情值加1。目前心情值为", self.mood_index, "，活力值为", self.vitality, "，谢谢您给", self.name, "水。")
        else:
            self.heart -= 1
            print("失败！", self.name, "还剩", self.heart, "颗心。")
            # 判断还有没有心
            if self.check_heart():
                self.die("模拟人没有心了")

    # 定义Person类的sleep()方法，作用是让模拟人睡觉
    def sleep(self, time):
        print(self.name, "困了，请您让", self.name, "睡觉吧！")
        if input("请输入sleep：") == "sleep":
            print("成功！请等待", time, "秒。")
            # 显示一个进度条
            for _ in trange(time):
                sleep(1)
                pass
            print(self.name, "睡饱了，心情值加3。目前心情值为", self.mood_index, "，活力值为", self.vitality, "，谢谢你给", self.name, "食物。")
            self.mood_index += 3
        else:
            self.heart -= 1
            print("失败！", self.name, "还剩", self.heart, "颗心。")
            # 判断还有没有心
            if self.check_heart():
                self.die("模拟人没有心了")

    # 定义Person类的birthday()方法，作用是让模拟人过生日
    def birthday(self):
        self.age += 1
        if self.age < 18:
            self.height += randint(2, 4)
            self.weight += randint(2, 4)
        print("恭喜！现在", self.name, self.age, "岁了，身高是", self.height, "厘米，体重是", self.weight, "千克，心情值是", self.mood_index, "活力值是", self.vitality, "。")
        if input("输入quit退出游戏，输入其他字符继续游戏，请输入：") == "quit":
            self.alive = False
            print("好的，游戏结束。")
            sleep(3)
            exit()
        else:
            print("好的，游戏继续。")

    # 定义Person类的die()方法，作用是让模拟人死
    def die(self, reason):
        self.alive = False
        print("抱歉，", self.name, "死了，游戏结束。原因：", reason)
        sleep(3)
        exit()

    # 定义Person类的check_heart()方法，作用是检查模拟人的血量是否大于0
    def check_heart(self):
        if self.heart > 0:
            return True
        else:
            return False

    # 定义Person类的check_vitality()方法，作用是检查模拟人的活力值是否大于60
    def check_vitality(self):
        if self.vitality > 60:
            return True
        else:
            return False

    # 定义Person类的check_vitality()方法，作用是让模拟人的活力值每3秒减少1
    def reduce_vitality(self):
        while self.alive:
            if self.vitality > 0:
                person.vitality -= 1
                sleep(3)


# 主程序
print("\033[1;30;44m", end="")
print("欢迎来到模拟人类！这个游戏会模拟一个人，这个人一共有3颗心，如果不按要求操作就会扣1颗心，如果这个人的活力值小于60就会死亡")
person_name = input("请输入这个人的名字：")
if person_name == "":
    print("您未输入。将使用默认名字：张三")
    person_name = "张三"
person_sex = input("请输入这个人的性别（男或女）：")
if person_sex != "男" and person_sex != "女":
    print("您未输入或输入错误。将把性别设为：男")
    person_sex = "男"
person_height = randint(50, 60)
person_weight = randint(2, 4)
person = Person(person_name, person_sex, person_height, person_weight)
thread = Thread(target=person.reduce_vitality)
thread.start()
for _ in range(randint(55, 70)):
    person.eat(randint(10, 15))
    sleep(5)
    if not person.check_vitality():
        person.die("模拟人没有活力值了")
    person.drink(randint(2, 4))
    sleep(5)
    if not person.check_vitality():
        person.die("模拟人没有活力值了")
    person.sleep(randint(25, 30))
    sleep(5)
    if not person.check_vitality():
        person.die("模拟人没有活力值了")
    live_or_die = randint(1, 1000)
    if live_or_die >= 900:
        person.die("模拟人因为意外而死亡")
    else:
        person.birthday()
        sleep(5)
person.die("模拟人去世了")
