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