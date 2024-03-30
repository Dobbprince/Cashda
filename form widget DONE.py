from tkinter import *
from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("500x600+200+200")
win.title("Student Application")
win.configure(bg ="#A9DFBF")
win.resizable(False,False)

#add widgets
lbl = Label(win, text="Student Enrolment Form", font=('arial',14,'bold'),fg= 'Red',bg='#A9DFBF' )
#lbl.grid(row=2 , column=0)
#lbl.pack()
lbl.place(x=200 , y=50)


#REG NO
btn = Button(win, text="REG NO", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=45 , y=120)
win.configure(bg ="#A9DFBF")

display=Entry(win, width=30, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'))
display.place(x=140 , y=120)

#FIRST NAME
btn = Button(win, text="FIRST NAME", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=45 , y=165)
win.configure(bg ="#A9DFBF")

display=Entry(win, width=30, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'))
display.place(x=170 , y=165)

#LAST NAME
btn = Button(win, text="LAST NAME", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=45 , y=210)
win.configure(bg ="#A9DFBF")

display=Entry(win, width=30, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'))
display.place(x=170 , y=210)

#USERNAME
btn = Button(win, text="USERNAME", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=45 , y=250)
win.configure(bg ="#A9DFBF")

display=Entry(win, width=30, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'))
display.place(x=170 , y=250)

#PASSWORD
btn = Button(win, text="PASSWORD", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=45 , y=290)
win.configure(bg ="#A9DFBF")

display=Entry(win, width=30, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'))
display.place(x=170 , y=290)

#ADD
btn = Button(win, text="ADD", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=45 , y=350)

#SEARCH
btn = Button(win, text="SEARCH", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=100 , y=350)
win.configure(bg ="#A9DFBF")

#UPDATE
btn = Button(win, text="UPDATE", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=186 , y=350)

#DELETE
btn = Button(win, text="DELETE", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=270 , y=350)
win.configure(bg ="#A9DFBF")
