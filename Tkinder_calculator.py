from tkinter import *

window = Tk()
window.geometry("360x385")
window.resizable(0, 0)
window.configure(background="#696969")
window.title("Calculator By DVG") 



def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear():
    global expression
    expression = ""
    input_text.set("")


def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


expression = ""
input_text = StringVar()

input_frame = Frame(window, width=20, height=3, bd=2, highlightbackground="grey", highlightcolor="black",
                    highlightthickness=2)
input_frame.grid(column=0, row=0, columnspan=32, padx=5, pady=6)

input_field = Entry(input_frame, font=('arial', 19, 'bold'), textvariable=input_text, width=23, bg="#eee",
                    justify=RIGHT)
input_field.grid(row=0, column=0, ipady=15, ipadx=6)

button7 = Button(window, text="7", width=6, height=3, cursor="hand2", command=lambda: btn_click(7))
button7.grid(column=0, row=1, padx=10, pady=10)

button8 = Button(window, text="8", width=6, height=3, cursor="hand2", command=lambda: btn_click(8))
button8.grid(row=1, column=1, padx=10, pady=10)

button9 = Button(window, text="9", width=6, height=3, cursor="hand2", command=lambda: btn_click(9))
button9.grid(row=1, column=2, padx=10, pady=10)

button4 = Button(window, text="4", width=6, height=3, cursor="hand2", command=lambda: btn_click(4))
button4.grid(row=2, column=0, padx=10, pady=10)

button5 = Button(window, text="5", width=6, height=3, cursor="hand2", command=lambda: btn_click(5))
button5.grid(row=2, column=1, padx=10, pady=10)

button6 = Button(window, text="6", width=6, height=3, cursor="hand2", command=lambda: btn_click(6))
button6.grid(row=2, column=2, padx=10, pady=10)

button1 = Button(window, text="1", width=6, height=3, cursor="hand2", command=lambda: btn_click(1))
button1.grid(row=3, column=0, padx=10, pady=10)

button2 = Button(window, text="2", width=6, height=3, cursor="hand2", command=lambda: btn_click(2))
button2.grid(row=3, column=1, padx=10, pady=10)

button3 = Button(window, text="3", width=6, height=3, cursor="hand2", command=lambda: btn_click(3))
button3.grid(row=3, column=2, padx=10, pady=10)

dot = Button(window, text=".", width=6, height=3, cursor="hand2", command=lambda: btn_click("."))
dot.grid(row=4, column=0, padx=10, pady=10)

zero = Button(window, text="0", width=6, height=3, cursor="hand2", command=lambda: btn_click(0))
zero.grid(row=4, column=1, padx=10, pady=10)

twozero = Button(window, text="00", width=6, height=3, cursor="hand2", command=lambda: btn_click("00"))
twozero.grid(row=4, column=2, padx=10, pady=10)

clear = Button(window, text="Clr", width=6, height=3, cursor="hand2", command=lambda: bt_clear())
clear.grid(row=1, column=3, padx=10, pady=10)

add = Button(window, text="+", width=6, height=8, cursor="hand2", command=lambda: btn_click("+"))
add.grid(row=1, column=4, padx=10, pady=10, rowspan=2)

sub = Button(window, text="-", width=6, height=3, cursor="hand2", command=lambda: btn_click("-"))
sub.grid(row=3, column=4, padx=10, pady=10)

div = Button(window, text="/", width=6, height=3, cursor="hand2", command=lambda: btn_click("/"))
div.grid(row=2, column=3, padx=10, pady=10)

mul = Button(window, text="x", width=6, height=3, cursor="hand2", command=lambda: btn_click("*"))
mul.grid(row=3, column=3, padx=10, pady=10)

equal = Button(window, text="=", width=16, height=3, cursor="hand2", command=lambda: bt_equal())
equal.grid(row=4, column=3, padx=10, pady=10, columnspan=3)

window.mainloop()