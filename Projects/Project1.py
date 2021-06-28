import tkinter
from tkinter import filedialog, Text, mainloop
import os
from tkinter.constants import COMMAND, END, RIGHT
from functools import partial

root = tkinter.Tk()
displayed = []
operation = 'k'
r1 = 0
r2 = 0

def Operation(i):
    global r1
    r1 = float(dText.get("1.0", END))
    dText.delete("1.0", END)
    displayed.clear()
    global operation
    operation = i

def AddNumberToButton(x):
    displayed.append(x)
    dText.delete("1.0", END)
    x = ""
    x = x.join(str(displayed))
    y = x.replace(',', "").replace('[', "").replace(' ', '').replace(']', '')
    dText.insert(END , y)
    dText.pack()

def Clear():
    dText.delete("1.0", END)
    displayed.clear()

def Result():
    r2 = float(dText.get("1.0", END))

    if (operation == '+'):
        result = r1 + r2
        dText.delete("1.0", END)
        dText.insert(END , result)
        dText.pack()
        displayed.clear()
    if (operation == '-'):
        result = r1 - r2
        dText.delete("1.0", END)
        dText.insert(END , result)
        dText.pack()
        displayed.clear()
    if (operation == '*'):
        result = r1 * r2
        dText.delete("1.0", END)
        dText.insert(END , result)
        dText.pack()
        displayed.clear()
    if (operation == '/'):
        result = r1 / r2
        dText.delete("1.0", END)
        dText.insert(END , result)
        dText.pack()
        displayed.clear()

    else:
        r2 = 0
        print(operation)
        print("WORKING")



label = tkinter.Label(root, text="Calculator", foreground="black")
label.pack()

canvas = tkinter.Canvas(root, height=700, width=700, bg="#000000")
canvas.pack()

frame = tkinter.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.1)

dText = tkinter.Text(frame, width=50,height=40, font=("Arial", 32), fg="red")

button1 = tkinter.Button(root, bg="gray", text="1", command=partial(AddNumberToButton, 1))
button1.place(relwidth=0.15, relheight=0.1, relx=0.12, rely=0.4)

button2 = tkinter.Button(root, bg="gray", text="2", command=partial(AddNumberToButton, 2))
button2.place(relwidth=0.15, relheight=0.1, relx=0.32, rely=0.4)

button3 = tkinter.Button(root, bg="gray", text="3", command=partial(AddNumberToButton, 3))
button3.place(relwidth=0.15, relheight=0.1, relx=0.52, rely=0.4)

button4 = tkinter.Button(root, bg="gray", text="4", command=partial(AddNumberToButton, 4))
button4.place(relwidth=0.15, relheight=0.1, relx=0.12, rely=0.55)

button5 = tkinter.Button(root, bg="gray", text="5", command=partial(AddNumberToButton, 5))
button5.place(relwidth=0.15, relheight=0.1, relx=0.32, rely=0.55)

button6 = tkinter.Button(root, bg="gray", text="6", command=partial(AddNumberToButton, 6))
button6.place(relwidth=0.15, relheight=0.1, relx=0.52, rely=0.55)

button7 = tkinter.Button(root, bg="gray", text="7", command=partial(AddNumberToButton, 7))
button7.place(relwidth=0.15, relheight=0.1, relx=0.12, rely=0.7)

button8 = tkinter.Button(root, bg="gray", text="8", command=partial(AddNumberToButton, 8))
button8.place(relwidth=0.15, relheight=0.1, relx=0.32, rely=0.7)

button9 = tkinter.Button(root, bg="gray", text="9", command=partial(AddNumberToButton, 9))
button9.place(relwidth=0.15, relheight=0.1, relx=0.52, rely=0.7)

buttonMultiply = tkinter.Button(root, bg="gray", text="*", command=partial(Operation, '*'))
buttonMultiply.place(relwidth=0.15, relheight=0.1, relx=0.52, rely=0.25)

buttonClear = tkinter.Button(root, bg="gray", text="Clear", command=Clear)
buttonClear.place(relwidth=0.15, relheight=0.1, relx=0.72, rely=0.25)

buttonAdd = tkinter.Button(root, bg="gray", text="+", command=partial(Operation, '+'))
buttonAdd.place(relwidth=0.15, relheight=0.1, relx=0.72, rely=0.4)

buttonMinus = tkinter.Button(root, bg="gray", text="-", command=partial(Operation, '-'))
buttonMinus.place(relwidth=0.15, relheight=0.1, relx=0.72, rely=0.55)

buttonDivision = tkinter.Button(root, bg="gray", text="/", command=partial(Operation, '/'))
buttonDivision.place(relwidth=0.15, relheight=0.1, relx=0.72, rely=0.7)

buttonResult = tkinter.Button(root, bg="gray", text="=", command=Result)
buttonResult.place(relwidth=0.15, relheight=0.1, relx=0.72, rely=0.85)

root = mainloop()