from datetime import datetime as d
from time import sleep as s
t = d.now()
choice = input("""1：日期
2：时间
请问您想要查询日期还是时间：""")
if choice == "1":
    print(t.strftime("日期是%Y年%m月%d日"))
    s(3)
elif choice == "2":
    print(t.strftime("时间是%H时%M分%S秒"))
    s(3)
else:
    print("输入错误！")
    s(3)
