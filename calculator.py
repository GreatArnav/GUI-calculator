import tkinter as tk

window = tk.Tk()

# title of window
window.title("Arnav Calculator")
window.geometry("430x500")
window.configure(bg='white')
photo = tk.PhotoImage(file = "calculator.png")
window.iconphoto(False, photo)


txt = ''
output = tk.Label(window, text=txt, height=2, width=14, font=("Arial Bold", 25))
output.place(x=5, y=5)


# button function
def enter_num(num):
    global txt
    txt = txt+str(num)
    output = tk.Label(window, text=txt, height=2, width=14, font=("Arial Bold", 25))
    output.place(x=5, y=5)

# backspace
def backspace():
    global txt
    l = list(txt)
    length = len(l)-1
    l.remove(l[length])
    txt = ''.join(l)
    output = tk.Label(window, text=txt, height=2, width=14, font=("Arial Bold", 25))
    output.place(x=5, y=5)



# solve
def sovle():
    global txt
    ans = eval(txt)
    txt = str(ans)
    output = tk.Label(window, text=txt, height=2, width=14, font=("Arial Bold", 25))
    output.place(x=5, y=5)

# button
btn1 = tk.Button(window, text = ' 1', bd = '15',bg='yellow',command = lambda : [enter_num(1)],foreground="black",font=("Arial Bold",35))
btn1.place(x=10,y=90)

btn2 = tk.Button(window, text = ' 2', bd = '15',bg='yellow',command = lambda : [enter_num(2)],foreground="black",font=("Arial Bold",35))
btn2.place(x=120,y=90)

btn3 = tk.Button(window, text = ' 3', bd = '15',bg='yellow',command = lambda : [enter_num(3)],foreground="black",font=("Arial Bold",35))
btn3.place(x=230,y=90)

btn4 = tk.Button(window, text = ' 4', bd = '15',bg='yellow',command = lambda : [enter_num(4)],foreground="black",font=("Arial Bold",35))
btn4.place(x=10,y=190)

btn5 = tk.Button(window, text = ' 5', bd = '15',bg='yellow',command = lambda : [enter_num(5)],foreground="black",font=("Arial Bold",35))
btn5.place(x=120,y=190)

btn6 = tk.Button(window, text = ' 6', bd = '15',bg='yellow',command = lambda : [enter_num(6)],foreground="black",font=("Arial Bold",35))
btn6.place(x=230,y=190)

btn7 = tk.Button(window, text = ' 7', bd = '15',bg='yellow',command = lambda : [enter_num(7)],foreground="black",font=("Arial Bold",35))
btn7.place(x=10,y=290)

btn8 = tk.Button(window, text = ' 8', bd = '15',bg='yellow',command = lambda : [enter_num(8)],foreground="black",font=("Arial Bold",35))
btn8.place(x=120,y=290)

btn9 = tk.Button(window, text = ' 9', bd = '15',bg='yellow',command = lambda : [enter_num(9)],foreground="black",font=("Arial Bold",35))
btn9.place(x=230,y=290)

btn0 = tk.Button(window, text = ' 0', bd = '15',bg='yellow',command = lambda : [enter_num(0)],foreground="black",font=("Arial Bold",35))
btn0.place(x=120,y=390)

btn_dot = tk.Button(window, text = ' . ', bd = '15',bg='yellow',command = lambda : [enter_num('.')],foreground="black",font=("Arial Bold",35))
btn_dot.place(x=230,y=390)

btn_enter = tk.Button(window, text = 'Enter', bd = '15',bg='yellow',command = lambda : [sovle()],foreground="black",font=("Arial Bold",28))
btn_enter.place(x=287,y=0)

btn_mul = tk.Button(window, text = ' x', bd = '15',bg='gray',command = lambda : [enter_num('*')],foreground="black",font=("Arial Bold",35))
btn_mul.place(x=340,y=90)

btn_div = tk.Button(window, text = '  /', bd = '15',bg='gray',command = lambda : [enter_num('/')],foreground="black",font=("Arial Bold",35))
btn_div.place(x=340,y=190)

btn_plus = tk.Button(window, text = ' +', bd = '15',bg='gray',command = lambda : [enter_num('+')],foreground="black",font=("Arial Bold",35))
btn_plus.place(x=340,y=290)

btn_minus = tk.Button(window, text = '  -', bd = '15',bg='gray',command = lambda : [enter_num('-')],foreground="black",font=("Arial Bold",35))
btn_minus.place(x=340,y=390)

btn_del = tk.Button(window, text = 'del', bd = '20',bg='gray',command = lambda : [backspace()],foreground="black",font=("Arial Bold",20))
btn_del.place(x=10,y=390)

window.mainloop()
