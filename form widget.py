
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

def clear():
    regno.set("")
    lname.set("")
    uname.set("")
    pwd.set("")

def add():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="schooldb")
        cur=con.cursor()
        sql="insert into students values('%s','%s','%s','%s','%s')"%(regno.get(),fname.get(),lname.get(),uname.get(),pwd.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("success","congrats! your record was saved")
    except:
           messagebox.showerror('Error',"Ooops! Somthing went rong")
    finally:
           clear()

           
def search():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="schooldb")
        cur=con.cursor()
        sql="select * from students where regno='%s'"%regno.get() 
        cur.execute(sql)
        result=cur.fetchone()
        fname.set(result[1])
        lname.set(result[2])
        uname.set(result[3])
        pwd.set(result[4])  
        con.close()
        messagebox.showinfo("success","congrats!These is the election search results")
    except:
           messagebox.showerror('Error',"Ooops! Somthing went rong")
             

def update():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="schooldb")
        cur=con.cursor()
        sql="update students set firstname='%s',lastname='%s',username='%s',password='%s' where regno='%s'"%(fname.get(),lname.get(),uname.get(),pwd.get(),regno.get())        
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("success","congrats! your record was saved")
    except:
           messagebox.showerror('Error',"Ooops! Somthing went wrong")
    finally:
        clear()

def delete():
        try:
            con=pymysql.connect(host='localhost',user='root',password="",database="schooldb")
            cur=con.cursor()
            sql="delete from students where students = '$'"%(regno.get())
            cur.execute(sql)
            con.commit()
            con.close()
            messagebox.showinfo("success","congrats! your record was saved")
        except:
            messagebox.showerror('Error',"Ooops! Somthing went wrong")
        


win = Tk()
win.geometry("500x600+200+200")
win.title("Student Application")
win.configure(bg ="#A9DFBF")
win.resizable(False,False)

#Variables
regno=StringVar()
fname=StringVar()
lname=StringVar()
uname=StringVar()
pwd=StringVar()






#add widgets
lbl = Label(win, text="Student Enrolment Form", font=('arial',14,'bold'),fg= 'Red',bg='#A9DFBF' )
#lbl.grid(row=2 , column=0)
#lbl.pack()
lbl.place(x=140 , y=70)




#REG NO
btn = Button(win, text="REG NO", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=45 , y=120)
win.configure(bg ="#A9DFBF")

rgn=Entry(win, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=regno)
rgn.place(x=140 , y=120)

#FIRST NAME
btn = Button(win, text="FN", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=45 , y=165)
win.configure(bg ="#A9DFBF")

fn=Entry(win, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=fname)
fn.place(x=170 , y=165)

#LAST NAME
btn = Button(win, text="LN", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=45 , y=210)
win.configure(bg ="#A9DFBF")

ln=Entry(win, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=lname)
ln.place(x=170 , y=210)

#USERNAME
btn = Button(win, text="USERNAME", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=45 , y=250)
win.configure(bg ="#A9DFBF")

un=Entry(win, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=uname)
un.place(x=170 , y=250)

#PASSWORD
btn = Button(win, text="PASSWORD", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=45 , y=290)
win.configure(bg ="#A9DFBF")

pd=Entry(win, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),show='*',textvariable=pwd)
pd.place(x=170 , y=290)



#ADD
btna = Button(win, text="ADD", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=add)
btna.place(x=45 , y=350)

#SEARCH
btns = Button(win, text="SEARCH", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=search)
btns.place(x=100 , y=350)
win.configure(bg ="#A9DFBF")

#UPDATE
btnu = Button(win, text="UPDATE", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=update)
btnu.place(x=186 , y=350)

#DELETE
btnd = Button(win, text="DELETE", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=delete)
btnd.place(x=270 , y=350)
win.configure(bg ="#A9DFBF")

#Clear
btn = Button(win, text="CLEAR", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=clear)
btn.place(x=350 , y=350)
win.configure(bg ="#A9DFBF")

