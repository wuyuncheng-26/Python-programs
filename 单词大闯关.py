from tkinter import *
from time import *
from random import *


def choose_questions(questions_dictionary):
    question = choice(list(questions_dictionary))
    answer = questions_dictionary[question]
    return {question: answer}


def ask_question(window, question):
    label = Label(master=window, bg="red", fg="yellow", font=("楷体", 14), text=question)
    entry = Entry(master=window, bg="blue", fg="yellow", font=("楷体", 17), width=15)

    def get_player_answer():
        return entry.get()
    button = Button(master=window, bg="blue", command=get_player_answer, fg="red", font=("楷体", 12), text="确定")
    label.pack()
    entry.pack()
    button.pack()


root = Tk()
print(choose_questions({"test1": "test", "test2": "test"}))
print(ask_question(root, "test"))
root.mainloop()
