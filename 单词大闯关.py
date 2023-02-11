from tkinter import *
from time import *
from random import *


def choose_questions(questions_dictionary):
    question = choice(list(questions_dictionary))
    answer = questions_dictionary[question]
    return {question: answer}


def ask_question(window, question):
    label1 = Label(master=window, bg="red", fg="yellow", font=("楷体", 14), text=question)
    label2 = Label(master=window, bg="blue", fg="yellow", font=("楷体", 12), text="请在10秒内回答")
    entry = Entry(master=window, bg="blue", fg="yellow", font=("楷体", 17), width=15)
    label1.pack()
    label2.pack()
    entry.pack()
    sleep(10)
    return entry.get()


root = Tk()
print(choose_questions({"test1": "test", "test2": "test"}))
print(ask_question(root, "test"))
root.mainloop()
