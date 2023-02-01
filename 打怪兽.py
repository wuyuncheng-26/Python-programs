"""
当前版本为1.1

本版本主要内容：
给Pet类和Monster类添加了攻击力和防御力系统
"""
# 导入random，time和tqdm库中的部分函数
# tqdm库是第三方库，需要先在命令提示符里用pip来下载
from random import choice, randint
from time import sleep
from tqdm import trange


# 定义Pet类，来模拟一个宠物
class Pet:
    # 定义Pet类的__init__()方法，也就是Pet类的构造方法
    def __init__(self, name, number, hp, attack, defence):
        self.name = name
        self.number = number
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print("你的", self.number, "号宠物叫", self.name, "，血量是", self.hp, "，攻击力是", self.attack, "，防御力是", self.defence, "。")

    # 定义Pet类的attack()方法，作用是让宠物攻击敌人
    def attack_enemy(self, enemy):
        if enemy.hp > 0 and self.hp > 0:
            enemy.hp -= self.attack - enemy.defence
            # 判断有没有把敌人打死
            if enemy.hp <= 0:
                enemy.hp = 0
                print("你的", self.number, "号宠物把", enemy.number, "号怪物打死了。")
            else:
                print(self.number, "号宠物攻击了", enemy.number, "号怪兽。怪兽还剩余", enemy.hp, "点血。")
        elif self.hp == 0:
            print("宠物已经没血了，无法攻击。")
        else:
            print("怪兽已经没血了，无法攻击。")

    # 定义Pet类的rest()方法，作用是让宠物休息
    def rest(self):
        # 判断宠物的血量是否小于600且大于0
        if 600 > self.hp > 0:
            self.hp += randint(50, 80)
            # 判断宠物的血量是否小于600
            if self.hp < 600:
                print(self.name, "休息了一会儿，", self.name, "现有", self.hp, "点血。")
            else:
                self.hp = 600
                print(self.name, "休息了一会儿，", self.name, "现有", self.hp, "点血。")
        else:
            print(self.number, "号宠物的血量已经达到最高限制600或血量已经为0，无法回血。")


# 定义Monster类，来模拟一个怪兽
class Monster:
    # 定义Monster类的__init__()方法，也就是Monster类的构造方法
    def __init__(self, name, number, hp, attack, defence):
        self.name = name
        self.number = number
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print(self.number, "号怪兽叫", self.name, "，血量是", self.hp, "。")

    # 定义Monster类的attack()方法，作用是让怪物攻击敌人
    def attack_enemy(self, enemy, damage):
        if enemy.hp > 0 and self.hp > 0:
            enemy.hp -= self.attack - enemy.defence
            # 判断有没有把敌人打死
            if enemy.hp <= 0:
                enemy.hp = 0
                print("怪兽把你的", enemy.number, "号宠物打死了。")
            else:
                print(self.number, "号怪兽攻击了", enemy.number, "号宠物。宠物减少了", damage, "滴血，宠物还剩余", enemy.hp, "点血。")

    # 定义Monster类的rest()方法，作用是让怪物休息
    def rest(self):
        # 判断怪兽的血量是否小于250且大于0
        if 250 > self.hp > 0:
            self.hp += randint(20, 50)
            # 判断宠物的血量是否小于250
            if self.hp < 250:
                print(self.number, "号怪兽休息了一会儿，血量变成了", self.hp, "点血。")
            else:
                self.hp = 250
                print(self.number, "号怪兽休息了一会儿，血量变成了", self.hp, "点血。")


# 主程序
print("\033[1;30;44m", end="")
print("欢迎来到打怪兽，您需要控制宠物去打怪兽，加油吧！")
sleep(2)
p1 = Pet(choice(["Tom", "Eason", "Angela", "Jack", "Tim"]), 1, randint(450, 600), randint(35, 45), randint(20, 30))
p2 = Pet(choice(["Tom", "Eason", "Angela", "Jack", "Tim"]), 2, randint(450, 600), randint(35, 45), randint(20, 30))
p3 = Pet(choice(["Tom", "Eason", "Angela", "Jack", "Tim"]), 3, randint(450, 600), randint(35, 45), randint(20, 30))
sleep(2)
while True:
    m1 = Monster(choice(["Amy", "Jim", "Ben", "Alex", "Andy"]), 1, randint(150, 250), p1.attack * 0.6, p1.defence * 0.6)
    m2 = Monster(choice(["Amy", "Jim", "Ben", "Alex", "Andy"]), 2, randint(150, 250), p2.attack * 0.6, p2.defence * 0.6)
    m3 = Monster(choice(["Amy", "Jim", "Ben", "Alex", "Andy"]), 3, randint(150, 250), p3.attack * 0.6, p3.defence * 0.6)
    sleep(2)
    while m1.hp > 0 or m2.hp > 0 or m3.hp > 0:
        player_choice = input("""111:1号宠物攻击1号怪兽
112:1号宠物攻击2号怪兽
113:1号宠物攻击3号怪兽
12:1号宠物休息

211:2号宠物攻击1号怪兽
212:2号宠物攻击2号怪兽
213:2号宠物攻击3号怪兽
22:2号宠物休息

311:3号宠物攻击1号怪兽
312:3号宠物攻击2号怪兽
313:3号宠物攻击3号怪兽
32:3号宠物休息

请选择对宠物下达的命令：""")
        if player_choice == "111": p1.attack_enemy(m1)
        elif player_choice == "112": p1.attack_enemy(m2)
        elif player_choice == "113": p1.attack_enemy(m3)
        elif player_choice == "12": p1.rest()
        elif player_choice == "211": p2.attack_enemy(m1)
        elif player_choice == "212": p2.attack_enemy(m2)
        elif player_choice == "213": p2.attack_enemy(m3)
        elif player_choice == "22": p2.rest()
        elif player_choice == "311": p3.attack_enemy(m1)
        elif player_choice == "312": p3.attack_enemy(m2)
        elif player_choice == "313": p3.attack_enemy(m3)
        elif player_choice == "32": p3.rest()
        else: print("你没有输入正确的指令，请输入正确的指令。")

        if randint(1, 2) == 1:
            choice([m1, m2, m3]).attack_enemy(choice([p1, p2, p3]), randint(20, 40))
        else:
            choice([m1, m2, m3]).rest()
        sleep(3)
    m1.attack += 2
    m1.defence += 2
    m2.attack += 2
    m2.defence += 2
    m3.attack += 2
    m3.defence += 2
    if input("恭喜你打败了所有怪兽，宠物的攻击力和防御力加2。输入quit可以退出游戏，输入其他字符继续游戏。") == "quit":
        print("好的，游戏结束。")
        sleep(3)
        exit()
    else:
        print("好的，继续游戏。请你等待怪物刷新。")
        for i in trange(randint(20, 30)):
            sleep(1)
            pass
