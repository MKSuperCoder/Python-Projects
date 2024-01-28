from customtkinter import *
from tkinter import *

set_appearance_mode = "dark"
set_default_color_theme = "dark-blue"

def button_press(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""

CalculatorWindow = CTk()
CalculatorWindow.title("Calculator")
CalculatorWindow.geometry("300x460")

equation_text = ""
equation_label = StringVar(value = 0)

label = Label(CalculatorWindow, textvariable = equation_label, font=('arial', 20), bg="white", width=24, height=5)
label.pack()

frame = Frame(CalculatorWindow)
frame.pack()

button1 = Button(frame, text=7, height=4, width=9, font = 35, 
                 command = lambda: button_press(7))
button1.grid(row=1, column=0)

button2 = Button(frame, text=8, height=4, width=9, font = 35, 
                 command = lambda: button_press(8))
button2.grid(row=1, column=1)

button3 = Button(frame, text=9, height=4, width=9, font = 35, 
                 command = lambda: button_press(9))
button3.grid(row=1, column=2)
button4 = Button(frame, text=4, height=4, width=9, font = 35, 
                 command = lambda: button_press(4))
button4.grid(row=2, column=0)
button5 = Button(frame, text=5, height=4, width=9, font = 35, 
                 command = lambda: button_press(5))
button5.grid(row=2, column=1)
button6 = Button(frame, text=6, height=4, width=9, font = 35, 
                 command = lambda: button_press(6))
button6.grid(row=2, column=2)
button7 = Button(frame, text=1, height=4, width=9, font = 35, 
                 command = lambda: button_press(1))
button7.grid(row=3, column=0)
button8 = Button(frame, text=2, height=4, width=9, font = 35, 
                 command = lambda: button_press(2))
button8.grid(row=3, column=1)
button9 = Button(frame, text=3, height=4, width=9, font = 35, 
                 command = lambda: button_press(3))
button9.grid(row=3, column=2)
button0 = Button(frame, text=0, height=4, width=9, font = 35, 
                 command = lambda: button_press(0))
button0.grid(row=4, column=1)
divide = Button(frame, text='÷', height=4, width=9, font = 35, 
                 command = lambda: button_press('/'))
divide.grid(row=0, column=3)
minus = Button(frame, text='-', height=4, width=9, font = 35, 
                 command = lambda: button_press('-'))
minus.grid(row=2, column=3)
multiply = Button(frame, text='*', height=4, width=9, font = 35, 
                 command = lambda: button_press('*'))
multiply.grid(row=1, column=3)
plus = Button(frame, text='+', height=4, width=9, font = 35, 
                 command = lambda: button_press('+'))
plus.grid(row=3, column=3)
equal = Button(frame, text='=', height=4, width=9, font = 35, 
                 command = equals)
equal.grid(row=4, column=3)
decimal = Button(frame, text='.', height=4, width=9, font = 35, 
                 command = lambda: button_press('.'))
decimal.grid(row=4, column=2)
clear = Button(frame, text='AC', height=4, width=9, font = 35, 
                 command = clear)
clear.grid(row=0,column=0)

plus_slash_minus = Button(frame, text="+/-", height=4, width=9, font=35)
plus_slash_minus.grid(row=0,column=1)

percentage = Button(frame, text="%", height=4, width=9, font=35)
percentage.grid(row=0,column=2)


CalculatorWindow.mainloop()