import tkinter as tk

value = ""
# function calls when any number or operator button is pressed
def click(press):
    global value

    value = value + str(press)
    scvalue.set(value)

# finction call when equal button is pressed
def equalbutton():
    try:
        global value
        total = str(eval(value))
        scvalue.set(total)
        value = ""
    except:
        scvalue.set(" Error ")
        value = ""

# function call when clear button is pressed
def clear():
    global value
    value = ""
    scvalue.set("")

root = tk.Tk()

#  Creating Windows geometry, size, shape
root.geometry("350x500")
root.resizable(width=False, height=False)
root.configure(background="#808080")

# Title and Icon
root.title("Calculator") 
root.wm_iconbitmap('calci.ico')

# Entry widget for entring value
scvalue = tk.StringVar()
scvalue.set("")
tk.Entry(root, relief='groove', border='10', textvariable=scvalue, font=('lucida', '30', 'bold')).pack()

# Numbers and operators buttons
full = tk.Frame(root)  #main frame (every buttons are inside this frame)

f1 = tk.Frame(full, bg="#00aaaa")
B = tk.Button(f1, padx=10, text='7', command=lambda: click(7), font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
B = tk.Button(f1, padx=10, text='8', command=lambda: click(8), font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
B = tk.Button(f1, padx=10, text='9', command=lambda: click(9), font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
B = tk.Button(f1, padx=10, text='/', command=lambda: click("/"), font=('lucidy', '31', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
f1.pack()


f2 = tk.Frame(full, bg="#00aaaa")
B = tk.Button(f2, padx=10, text='4', command=lambda: click(4), font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
B = tk.Button(f2, padx=10, text='5', command=lambda: click(5), font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
B = tk.Button(f2, padx=10, text='6', command=lambda: click(6), font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
B = tk.Button(f2, padx=10, text='*', command=lambda: click("*"), font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
f2.pack()


f3 = tk.Frame(full, bg="#00aaaa")
B = tk.Button(f3, padx=10, text='1', command=lambda: click(1), font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
B = tk.Button(f3, padx=10, text='2', command=lambda: click(2), font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
B = tk.Button(f3, padx=10, text='3', command=lambda: click(3), font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
B = tk.Button(f3, padx=10, text='+', command=lambda: click("+"), font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
f3.pack()


f4 = tk.Frame(full, bg="#00aaaa")
B = tk.Button(f4, padx=10, text='0', command=lambda: click(0), font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
B = tk.Button(f4, padx=15, text='.', command=lambda: click("."), font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
B = tk.Button(f4, padx=10, text='=', command=equalbutton, font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
B = tk.Button(f4, padx=10, text='-', command=lambda: click("-"), font=('lucidy', '30', 'bold'))
B.pack(side=tk.LEFT, pady='7', padx='7')
f4.pack()

f5 = tk.Frame(full)
B = tk.Button(f5, text='Clear', relief='groove', bg='#888888', border=5, command=clear, font=('lucidy', '20', 'bold'))
B.pack(fill=tk.X)
f5.pack(fill=tk.X)


full.pack()


root.mainloop()  #End of loop