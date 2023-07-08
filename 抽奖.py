from time import sleep
from tkinter import *
from random import choice
prize = ["巧克力", "冰激凌", "书", "玩具"]


def raffle(event):
    root.destroy()
    print(f"你抽到了{choice(prize)}")
    sleep(3)


root = Tk()
root.geometry("200x200+350+350")
root.title("抽奖")
label = Label(root, text="请选择")
label.pack()
button1 = Button(master=root, text="1")
button1.pack()
button2 = Button(master=root, text="2")
button2.pack()
button3 = Button(master=root, text="3")
button3.pack()
button4 = Button(master=root, text="4")
button4.pack()
button1.bind("<Button-1>", raffle)
button2.bind("<Button-1>", raffle)
button3.bind("<Button-1>", raffle)
button4.bind("<Button-1>", raffle)
root.mainloop()
