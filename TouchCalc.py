'''
TouchCalc By William Caffee

This is a simple calculator modified from a Tkinter example.

'''


from tkinter import *
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
    

def equalpress():
    try:
        
        global expression
        
        total = str(eval(expression))
        
        equation.set(total)
        expression = ""
        
    except:
        equation.set(" error ")
        expression = ""
    
def clear():
    global expression
    expression = ""
    equation.set("")
    
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="steel blue")
    gui.title("TouchCalc")
    gui.geometry("495x495")
    gui.grid_rowconfigure(tuple(range(5)), weight=1,)
    gui.grid_columnconfigure(tuple(range(4)), weight=1,)
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation, font=('Arial', 50))
    expression_field.grid(rowspan=1, columnspan=6, padx=13, sticky="NSEW")
        
    button1 = Button(gui, text=' 1 ', font=('Arial',25), fg='black', bg='red',
                         command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0, sticky="NSEW")
        
    button2 = Button(gui, text=' 2 ', font=('Arial',25), fg='black', bg='red',
                         command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1, sticky="NSEW")
        
    button3 = Button(gui, text=' 3 ', font=('Arial',25), fg='black', bg='red',
                         command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2, sticky="NSEW")
        
    button4 = Button(gui,text=' 4 ', font=('Arial',25), fg='black', bg='red',
                         command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0, sticky="NSEW")
        
    button5 = Button(gui, text=' 5 ', font=('Arial',25), fg='black', bg='red',
                         command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1, sticky="NSEW")
        
    button6 = Button(gui, text=' 6 ', font=('Arial', 25) , fg='black', bg='red',
                         command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2, sticky="NSEW")
        
    button7 = Button(gui, text=' 7 ', font=('Arial',25), fg='black', bg='red',
                         command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0, sticky="NSEW")
        
    button8 = Button(gui, text=' 8 ', font=('Arial',25), fg='black', bg='red',
                         command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1, sticky="NSEW")
        
    button9 = Button(gui, text=' 9 ', font=('Arial',25), fg='black', bg='red',
                         command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2, sticky="NSEW")
        
    button0 = Button(gui, text=' 0 ', font=('Arial',25), fg='black', bg='red',
                         command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0, sticky="NSEW")
        
    plus = Button(gui, text=' + ', font=('Arial',25), fg='black', bg='yellow',
                      command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3, sticky="NSEW")
        
    minus = Button(gui, text=' - ', font=('Arial',25), fg='black', bg='yellow',
                       command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3, sticky="NSEW")
        
    multiply = Button(gui, text=' x ', font=('Arial',25), fg='black', bg='yellow',
                          command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3, sticky="NSEW")
        
    divide = Button(gui, text=' / ', font=('Arial',25), fg='black', bg='yellow',
                        command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3, sticky="NSEW")
        
    equal = Button(gui, text=' = ', font=('Arial',25), fg='black', bg='green',
                       command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2, sticky="NSEW")
        
    clear = Button(gui, text='clear', font=('Arial',25), fg='black', bg='white',
                       command=clear, height=1, width=7)
    clear.grid(row=5, column=1, sticky="NSEW")
        
    Decimal = Button(gui, text='.', font=('Arial',30), fg='black', bg='yellow',
                         command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=3, sticky="NSEW")
        
gui.mainloop()
        
        
                       