import tkinter
import os
import webbrowser

window=tkinter.Tk()

window.title("Shortcut Launcher")
window.geometry("800x200+400+200")
window.resizable(False, False)

def notepad():
    os.system('notepad.exe')

def calc():
    os.system('calc.exe')

def folder():
    os.startfile('c:')

def google():
    url = "https://www.google.co.kr/"
    webbrowser.open(url)

btn1 = tkinter.Button(window, text="M", width=10, overrelief="solid", command=notepad)
btn2 = tkinter.Button(window, text="C", width=10, overrelief="solid", command=calc)
btn3 = tkinter.Button(window, text="F", width=10, overrelief="solid", command=folder)
btn4 = tkinter.Button(window, text="G", width=10, overrelief="solid", command=google)

btn5 =tkinter.Button(window, text=" ", width=10)
btn6 =tkinter.Button(window, text=" ", width=10)
btn7 =tkinter.Button(window, text=" ", width=10)
btn8 =tkinter.Button(window, text=" ", width=10)


btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=0, column=3)

btn5.grid(row=1, column=0)
btn6.grid(row=1, column=1)
btn7.grid(row=1, column=2)
btn8.grid(row=1, column=3)

window.mainloop()
