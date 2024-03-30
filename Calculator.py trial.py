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

1 #7,8,9,+,%
txtDisplay=Entry(cal,font=("arial",16,"bold"),textvariable=text_Input,insertwidth=4,bg="#E8F6F3",justify="right")
txtDisplay.grid(columnspan=4)

btn7=Button(cal, font=("arial", 12, "bold"), text="7",command=lambda:btnClick(7))
btn7.grid(row=1,column=0)

btn8=Button(cal, font=("arial", 12, "bold"), text="8",command=lambda:btnClick(8))
btn8.grid(row=1, column=1)

btn9=Button(cal, font=("arial", 12, "bold"), text="9",command=lambda:btnClick(9))
btn9.grid(row=1,column=2)

Addition=Button(cal,font=('arial', 12,'bold'), text="+",command=lambda:btnClick("+"))
Addition.grid(row=1,column=3)

Percent=Button(cal,font=('arial', 12,'bold'), text="%",command=lambda:btnClick("%"))
Percent.grid(row=1,column=4)

2 #4,5,6,-,‰
btn4=Button(cal, font=("arial", 12, "bold"), text="4",command=lambda:btnClick(4))
btn4.grid(row=2,column=0)

btn5=Button(cal, font=("arial", 12, "bold"), text="5",command=lambda:btnClick(5))
btn5.grid(row=2, column=1)

btn6=Button(cal, font=("arial", 12, "bold"), text="6",command=lambda:btnClick(6))
btn6.grid(row=2,column=2)

Subtraction=Button(cal,font=('arial', 12,'bold'), text="-",command=lambda:btnClick("-"))
Subtraction.grid(row=2,column=3)

Radians=Button(cal,font=('arial',12,'bold'), text="Rad",command=lambda:btnClick(Radians))
Radians.grid(row=2,column=4)

3 #1,2,3-,x,.
btn1=Button(cal,font=("arial", 12, "bold"), text="1",command=lambda:btnClick(1))
btn1.grid(row=3, column=0)

btn2=Button(cal,font=("arial", 12, "bold"), text="2",command=lambda:btnClick(2))
btn2.grid(row=3, column=1)

btn3=Button(cal,font=("arial", 12, "bold"), text="3",command=lambda:btnClick(3))
btn3.grid(row =3, column=2)

Mutiply=Button(cal,font=('arial', 12,'bold'), text="*",command=lambda:btnClick("*"))
Mutiply.grid(row=3,column=3)

btnPeriod=Button(cal,font=("arial", 12, "bold"), text=".",command=lambda:btnClick("."))
btnPeriod.grid(row=3, column=4)


4 #0,C,=,/,.
btn0=Button(cal,font=("arial", 12, "bold"), text="0",command=lambda:btnClick(0))
btn0.grid(row=4, column=0)

btnC=Button(cal,font=("arial", 12, "bold"), text="C",command=btnClear)
btnC.grid(row=4, column=1)

btnEqual=Button(cal,font=("arial", 12, "bold"), text="=",command=btnEqual)
btnEqual.grid(row =4, column=2)

Divide=Button(cal,font=('arial', 12,'bold'), text="/",command=lambda:btnClick("/"))
Divide.grid(row =4, column=3)

btnParentheses =Button(cal,font=("arial", 12, "bold"), text="( )",command=lambda:btnClick("()"))
btnParentheses.grid(row =4, column=4)

5 #>,≥,≤,<,[]
btnStrictInequality=Button(cal,font=("arial", 12, "bold"), text=">",command=lambda:btnClick(">"))
btnStrictInequality.grid(row=5, column=0)

btnInequality=Button(cal,font=("arial", 12, "bold"), text="≥",command=lambda:btnClick("≥"))
btnInequality.grid(row=5, column=1)

btnInequality=Button(cal,font=("arial", 12, "bold"), text="≤",command=lambda:btnClick("≤"))
btnInequality.grid(row=5, column=2)

btnStrictInequality=Button(cal,font=("arial", 12, "bold"), text="<",command=lambda:btnClick("<"))
btnStrictInequality.grid(row=5, column=3)

brackets=Button(cal,font=('arial', 12,'bold'), text="[ ]",command=lambda: btnClick("[]"))
brackets.grid(row=5,column=4)


6 #a^b,√,√a,3√a
btnCaret=Button(cal,font=("arial", 12, "bold"), text="a^b",command=lambda:btnClick("a^b"))
btnCaret.grid(row =6, column=2)

SquareRoot=Button(cal,font=('arial', 12,'bold'), text="√",command=lambda:btnClick("√"))
SquareRoot.grid(row=6,column=3)

SquareRoot=Button(cal,font=('arial', 12,'bold'), text="√a",command=lambda:btnClick("√a"))
SquareRoot.grid(row=6,column=4)

CubeRoot=Button(cal,font=('arial',12,'bold'), text="3√a",command=lambda:btnClick("3√a"))
CubeRoot.grid(row=6,column=5)


8 #∠ ,∟,°,π,3√a
btnAngle =Button(cal,font=("arial", 12, "bold"), text="∠",command=lambda:btnClick("∠"))
btnAngle.grid(row =7, column=0)

RightAngle=Button(cal,font=('arial', 12,'bold'), text="∟",command=lambda:btnClick("∟"))
RightAngle.grid(row=7,column=1)

btndegree=Button(cal,font=("arial", 12, "bold"), text="°",command=lambda:btnClick("°"))
btndegree.grid(row =7, column=2)

PiConstant=Button(cal,font=('arial', 12,'bold'), text="π",command=lambda:btnClick("π"))
PiConstant.grid(row=7,column=3)

btnPermille=Button(cal,font=("arial", 12, "bold"), text="‰")
btnPermille.grid(row=7, column=4)

9 #∆,∑
btnDelta=Button(cal, font=("arial",12,"bold"), text="∆")
btnDelta.grid(row=9, column=0)

btnSigma=Button(cal, font=("arial", 12, "bold"), text="∑")
btnSigma.grid(row=9,column=1)

cal.mainloop()
