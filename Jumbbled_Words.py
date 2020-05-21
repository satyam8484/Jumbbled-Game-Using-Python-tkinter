from tkinter import *
import random
from tkinter import messagebox

# you can add more words as per your requirement
answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
    "FLOP",
    "HOPE",
    "TRIP",
    "LOVE",
    "FINISH",
    "POUND",
    "AWESOME",
    "sample",
    "tree",
    "respect",
    "book",
    "box",
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
    "LOPF",
    "PEHO",
    "IPTR",
    "OVLE",
    "SHIINF",
    "OUNOP",
    "MOAWEES",
    "maples",
    "rete",
    "sceptre",
    "kobo",
    "xob",
]

num = random.randrange(0, len(words), 1)


def Default():
    global words, answers, num
    l1.config(text=words[num])


def Check_Ans():
    global words, answers, num
    if (answers[num].lower() == e1.get().lower()):
        messagebox.showinfo("Congratulation", 'Your Answer is Correct')
        Res()
    else:
        messagebox.showerror("Error", 'Sorry, Your Answer is inCorrect')
        e1.delete(0, END)


def Res():
    global words, answers, num
    num = random.randrange(0, len(words), 1)
    l1.config(text=words[num])
    e1.delete(0, END)


window = Tk()
window.title('Jumbbled Word')
window.geometry('350x400+400+300')
window.configure(background='#000000')

l1 = Label(window,
           text='Your Text',
           font=('Verdana', 18),
           bg='#000000',
           fg='#ffffff',
           )
l1.pack(pady=30, ipadx=10, ipady=10)

ans1 = StringVar()
e1 = Entry(
    window,
    font=('Verdana', 16),
    textvariable=ans1,
)
e1.pack(ipadx=5, ipady=5)

btnchecked = Button(
    text='Check',
    font=('Comic Sans MS', 16),
    width=16,
    fg='#6ab04c',
    bg='#4C4B4B',
    relief=GROOVE,
    command=Check_Ans,
)
btnchecked.pack(pady=40)

btnreset = Button(
    text='Reset',
    font=('Comic Sans MS', 16),
    width=16,
    fg='#EA425C',
    bg='#4C4B4B',
    relief=GROOVE,
    command=Res,
)
btnreset.pack()

Default()
window.mainloop()
