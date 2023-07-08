from random import randint
from time import sleep
n = int(input("""1：加法题
2：减法题
3：乘法题
4：除法题

请问您要生成什么题目："""))
if n == 1:
    a = randint(1000, 4999)
    b = randint(1000, 4999)
    print(f"{a}+{b}")
    if input("输入“answer”查看答案：") == "answer":
        print(f"答案是：{a + b}")
    else:
        print("输入错误！")
        sleep(1)
elif n == 2:
    a = randint(1000, 4999)
    b = randint(1000, a)
    print(f"{a}-{b}")
    if input("输入“answer”查看答案：") == "answer":
        print(f"答案是：{a - b}")
    else:
        print("输入错误！")
        sleep(1)
elif n == 3:
    a = randint(10, 99)
    b = randint(10, 99)
    print(f"{a}×{b}")
    if input("输入“answer”查看答案：") == "answer":
        print(f"答案是：{a * b}")
    else:
        print("输入错误！")
        sleep(1)
elif n == 4:
    a = randint(10000, 49999)
    b = randint(10, 99)
    print(f"{a}÷{b}")
    if input("输入“answer”查看答案：") == "answer":
        print(f"答案是：{a // b}……{a % b}")
    else:
        print("输入错误！")
        sleep(1)
else:
    print("输入错误！")
    sleep(1)