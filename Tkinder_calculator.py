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