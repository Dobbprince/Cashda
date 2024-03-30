from tkinter import *
#functions here
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator=""
    text_Input.set("")

def btnEqual():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
    

cal = Tk()
cal.title("CashDaniel Calculator")
cal.resizable(False,False)
#cal.geometry("300x300+200+200")

#Global variable here
operator=""
text_Input=StringVar()

1 #7,8,9,+

txtDisplay=Entry(cal,font=("arial",16,"bold"), textvariable=text_Input,insertwidth=4,bg="#E8F6F3",justify="right")
txtDisplay.grid(columnspan=4)

btn7=Button(cal, font=("arial", 12, "bold"), text="7",command=lambda:btnClick(7))
btn7.grid(row=1,column=0)

btn8=Button(cal, font=("arial", 12, "bold"), text="8",command=lambda:btnClick(8))
btn8.grid(row=1, column=1)

btn9=Button(cal, font=("arial", 12, "bold"), text="9",command=lambda:btnClick(9))
btn9.grid(row=1,column=2)

Addition=Button(cal,font=('arial', 12,'bold'), text="+",command=lambda:btnClick("+"))
Addition.grid(row=1,column=3)

2 #4,5,6,-
btn4=Button(cal, font=("arial", 12, "bold"), text="4",command=lambda:btnClick(4))
btn4.grid(row=2,column=0)

btn5=Button(cal, font=("arial", 12, "bold"), text="5",command=lambda:btnClick(5))
btn5.grid(row=2, column=1)

btn6=Button(cal, font=("arial", 12, "bold"), text="6",command=lambda:btnClick(6))
btn6.grid(row=2,column=2)

Subtraction=Button(cal,font=('arial', 12,'bold'), text="-",command=lambda:btnClick("-"))
Subtraction.grid(row=2,column=3)

3 #1,2,3-,x
btn1=Button(cal,font=("arial", 12, "bold"), text="1",command=lambda:btnClick(1))
btn1.grid(row=3, column=0)

btn2=Button(cal,font=("arial", 12, "bold"), text="2",command=lambda:btnClick(2))
btn2.grid(row=3, column=1)

btn3=Button(cal,font=("arial", 12, "bold"), text="3",command=lambda:btnClick(3))
btn3.grid(row =3, column=2)

Mutiply=Button(cal,font=('arial', 12,'bold'), text="*",command=lambda:btnClick("*"))
Mutiply.grid(row=3,column=3)

4 #0,C,=,/
btn0=Button(cal,font=("arial", 12, "bold"), text="0",command=lambda:btnClick(0))
btn0.grid(row=4, column=0)

btnC=Button(cal,font=("arial", 12, "bold"), text="C",command=btnClear)
btnC.grid(row=4, column=1)

btnEqual=Button(cal,font=("arial", 12, "bold"), text="=",command=btnEqual)
btnEqual.grid(row =4, column=2)

Divide=Button(cal,font=('arial', 12,'bold'), text="/",command=lambda:btnClick("/"))
Divide.grid(row =4, column=3)

cal.mainloop()
