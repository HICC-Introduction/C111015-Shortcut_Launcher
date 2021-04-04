import tkinter
import os
import webbrowser
import tkinter.colorchooser as cl

window = tkinter.Tk() # 프로그램 기본 창 생성

# 프로그램 기본 창 사이즈
window_width = 800
window_height = 200
window_start_x = 400
window_start_y = 200

window.title('Shortcut Launcher')
window.geometry("%dx%d+%d+%d" % (window_width, window_height, window_start_x, window_start_y))
window.resizable(True, True)
window.wm_attributes("-topmost", 1)

def color_change(): # 프로그램 색상 지정
    color=cl.askcolor()
    print(color)
    window['bg'] = color[1]

def pop_up(): # 새로운 창 생성
    new_window = tkinter.Toplevel()
    new_window.title('프로그램 설정')
    new_window.geometry('300x300+100+10')
    btn = tkinter.Button(new_window, text="Color", width=20, height=3, overrelief="solid", command=color_change)
    btn.grid(row=3, column=3)

def close(): # 프로그램 종료
    window.quit()
    window.destroy()

# 프로그램 메뉴바 구성
menu_bar=tkinter.Menu(window)

menu_1=tkinter.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='메뉴', menu=menu_1)
menu_1.add_command(label='프로그램 설정', command=pop_up)
menu_1.add_command(label='프로그램 정보')
menu_1.add_separator()
menu_1.add_command(label='종료', command=close)

window.config(menu=menu_bar)

def notepad(): # 메모장 실행
    os.system('notepad.exe')

def calc(): # 계산기 실행
    os.system('calc.exe')

def folder(): # 폴더 열기 실행
    os.startfile('c:')

def google(): # 구글 열기 실행
    url = 'https://www.google.co.kr/'
    webbrowser.open(url)

# 버튼 개수
btn_row = 2
btn_column = 4

# 버튼 생성
btn1 = tkinter.Button(window, text="M", width=15, height=5, overrelief="solid", command=notepad)
btn2 = tkinter.Button(window, text="C", width=15, height=5, overrelief="solid", command=calc)
btn3 = tkinter.Button(window, text="F", width=15, height=5, overrelief="solid", command=folder)
btn4 = tkinter.Button(window, text="G", width=15, height=5, overrelief="solid", command=google)

btn5 = tkinter.Button(window, text=" ", width=15, height=5, overrelief="solid")
btn6 = tkinter.Button(window, text=" ", width=15, height=5, overrelief="solid")
btn7 = tkinter.Button(window, text=" ", width=15, height=5, overrelief="solid")
btn8 = tkinter.Button(window, text=" ", width=15, height=5, overrelief="solid")

# 버튼 위치
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=0, column=3)

btn5.grid(row=1, column=0)
btn6.grid(row=1, column=1)
btn7.grid(row=1, column=2)
btn8.grid(row=1, column=3)

window.mainloop()
