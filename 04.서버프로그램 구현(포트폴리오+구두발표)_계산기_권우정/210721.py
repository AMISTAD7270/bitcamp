from tkinter import *
from tkinter import font

top = Tk()
top.title("계산기")
top.configure(background='#AFDDFA')
top.geometry("435x450")

buttonFont = font.Font(family='Helvetica', size=16, weight='bold')

def cal():
    val = Entry.get(display)
    result = eval(val)
    display.delete(0, END)
    display.insert(0, result)


def cal1(e):
    val = Entry.get(display)
    result = eval(val)
    display.delete(0, END)
    display.insert(0, result)


def clear(pos):
    display.delete(0, END)


def b_press(val):
    display.insert("end", val)


def ce():
    ms = Entry.get(display)
    x = ''
    for i in range(len(ms) - 1):
        x += ms[i]

    display.delete(0, END)
    display.insert(0, x)


def ver():
    my = Entry.get(display)
    v = int(my) * -1
    display.delete(0, END)
    display.insert(0, v)


display = Entry(top, width=28, font=('Helvetica', 20), justify="right")
display.focus_set()

b_my = Button(top, text='EXIT', width=6, height=2, font=buttonFont, fg='#ffffff', bg='#CD1039', command=top.destroy)
b_c = Button(top, text='C', width=6, height=2, font=buttonFont, fg='#ffffff', bg='#FF7E9D', command=lambda: clear(END))
b_ce = Button(top, text='CE', width=6, height=2, font=buttonFont, fg='#ffffff', bg='#FF7E9D', command=ce)
b_e = Button(top, text='=', width=6, height=2, font=buttonFont, fg='#ffffff', bg='#FFA2AD', command=cal)

b_1 = Button(top, text='1', width=6, height=2, font=buttonFont, command=lambda: b_press('1'))
b_2 = Button(top, text='2', width=6, height=2, font=buttonFont, command=lambda: b_press('2'))
b_3 = Button(top, text='3', width=6, height=2, font=buttonFont, command=lambda: b_press('3'))
b_a = Button(top, text='+', width=6, height=2, font=buttonFont, fg='#ffffff', bg='#FFA2AD', command=lambda: b_press('+'))

b_4 = Button(top, text='4', width=6, height=2, font=buttonFont, command=lambda: b_press('4'))
b_5 = Button(top, text='5', width=6, height=2, font=buttonFont, command=lambda: b_press('5'))
b_6 = Button(top, text='6', width=6, height=2, font=buttonFont, command=lambda: b_press('6'))
b_s = Button(top, text='-', width=6, height=2, font=buttonFont, fg='#ffffff', bg='#FFA2AD', command=lambda: b_press('-'))

b_7 = Button(top, text='7', width=6, height=2, font=buttonFont, command=lambda: b_press('7'))
b_8 = Button(top, text='8', width=6, height=2, font=buttonFont, command=lambda: b_press('8'))
b_9 = Button(top, text='9', width=6, height=2, font=buttonFont, command=lambda: b_press('9'))
b_m = Button(top, text='×', width=6, height=2, font=buttonFont, fg='#ffffff', bg='#FFA2AD', command=lambda: b_press('*'))

b_v = Button(top, text='+/-', width=6, height=2, font=buttonFont, command=ver)
b_0 = Button(top, text='0', width=6, height=2, font=buttonFont, command=lambda: b_press('0'))
b_p = Button(top, text='.', width=6, height=2, font=buttonFont, command=lambda: b_press('.'))
b_d = Button(top, text='÷', width=6, height=2, font=buttonFont, fg='#ffffff', bg='#FFA2AD', command=lambda: b_press('/'))

display.grid(row=0, column=0, columnspan=4, pady=12, padx=6)

b_my.grid(row=1, column=0, pady=5)
b_c.grid(row=1, column=1)
b_ce.grid(row=1, column=2)
b_e.grid(row=1, column=3)

b_1.grid(row=2, column=0, pady=5)
b_2.grid(row=2, column=1)
b_3.grid(row=2, column=2)
b_a.grid(row=2, column=3)

b_4.grid(row=3, column=0, pady=5)
b_5.grid(row=3, column=1)
b_6.grid(row=3, column=2)
b_s.grid(row=3, column=3)

b_7.grid(row=4, column=0, pady=5)
b_8.grid(row=4, column=1)
b_9.grid(row=4, column=2)
b_m.grid(row=4, column=3)

b_v.grid(row=5, column=0, pady=5)
b_0.grid(row=5, column=1)
b_p.grid(row=5, column=2)
b_d.grid(row=5, column=3)

top.bind('<Return>', cal1)

top.mainloop()
