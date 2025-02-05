from customtkinter import *


def set_num(n):
    entry.insert(END,n)

res=0
def operation():
    global op
    op = entry.get()
    try:
        res = eval(op)
        entry.delete(0,END)
        entry.insert(0,res)
    except:
        operand = op.split("_%_")
        x = int(operand[0])
        y = int(operand[1])
        res = (x*y)/100
        entry.delete(0,END)
        entry.insert(0,res)

def clear():
    entry.delete(0,END)

def backSpace():
    global op
    op = entry.get()
    for i in range(len(op)):
        q=op[:-1]
    entry.delete(0,END)
    entry.insert(0,q)


calc = CTk()

calc.title("Calculator")

calc.minsize(370,450)
calc.geometry("370x450")
calc.maxsize(370,450)


# configure the grid
calc.columnconfigure(0, weight=1)
calc.rowconfigure(0, weight=1)
calc.columnconfigure(1, weight=1)
calc.rowconfigure(1, weight=4)
calc.columnconfigure(2, weight=1)
calc.rowconfigure(2, weight=4)
calc.columnconfigure(3, weight=1)
calc.rowconfigure(3, weight=4)
calc.rowconfigure(4, weight=4)
calc.rowconfigure(5, weight=4)


entry = CTkEntry(calc,font=("Agency FB",25,"bold"),width=340)
entry.icursor(END) 
entry.grid(column=0,row=0,columnspan=4,sticky=W,padx=14,pady=20)



btn_C = CTkButton(calc,text="C",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=clear)
btn_C.grid(column=0,row=1)

btn_7 = CTkButton(calc,text="7",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("7"))
btn_7.grid(column=0,row=2)

btn_4 = CTkButton(calc,text="4",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("4"))
btn_4.grid(column=0,row=3)

btn_1 = CTkButton(calc,text="1",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("1"))
btn_1.grid(column=0,row=4)

btn_00 = CTkButton(calc,text="00",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("00"))
btn_00.grid(column=0,row=5)



btn_per = CTkButton(calc,text="%",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("_%_"))
btn_per.grid(column=1,row=1)

btn_8 = CTkButton(calc,text="8",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("8"))
btn_8.grid(column=1,row=2)

btn_5 = CTkButton(calc,text="5",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("5"))
btn_5.grid(column=1,row=3)

btn_2 = CTkButton(calc,text="2",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("2"))
btn_2.grid(column=1,row=4)

btn_0 = CTkButton(calc,text="0",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("0"))
btn_0.grid(column=1,row=5)




btn_back = CTkButton(calc,text="<<",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=backSpace)
btn_back.grid(column=2,row=1)

btn_9 = CTkButton(calc,text="9",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("9"))
btn_9.grid(column=2,row=2)

btn_6 = CTkButton(calc,text="6",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("6"))
btn_6.grid(column=2,row=3)

btn_3 = CTkButton(calc,text="3",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("3"))
btn_3.grid(column=2,row=4)

btn_dot = CTkButton(calc,text=".",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("."))
btn_dot.grid(column=2,row=5)



btn_C = CTkButton(calc,text="/",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("/"))
btn_C.grid(column=3,row=1)

btn_8 = CTkButton(calc,text="X",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("*"))
btn_8.grid(column=3,row=2)

btn_5 = CTkButton(calc,text="-",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("-"))
btn_5.grid(column=3,row=3)

btn_2 = CTkButton(calc,text="+",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=lambda:set_num("+"))
btn_2.grid(column=3,row=4)

btn_0 = CTkButton(calc,text="=",font=("Agency FB",25,"bold"),width=75,fg_color="cyan",text_color="blue",command=operation)
btn_0.grid(column=3,row=5)

calc.mainloop()
