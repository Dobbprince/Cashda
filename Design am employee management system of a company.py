

from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


#function area
def clear():
    uid.set("")
    name.set("")
    post.set("")
    salary.set("")
    address.set("")
    

def register():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="dobbnet")
        cur=con.cursor()
        sql="insert into emdb(uid,name,post,salary,address) values('%s','%s','%s','%s','%s')"%(uid.get(),name.get(),post.get(),salary.get(),address.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("success","congrats!employee records is saved")
    except:
           messagebox.showerror('Error',"Ooops! Somthing went wrong")
    

def search():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="emdb")
        cur=con.cursor()
        sql="select * from emdb where id='%s'"%id.get()
        cur.execute(sql)
        result=cur.fetchone()
        id.set(result[1])
        name.set(result[2])
        post.set(result[3])
        salary.set(result[4])
        
        con.close()
        messagebox.showinfo("success","congrats!These is the employee search results")
    except:
           messagebox.showerror('Error',"Ooops! Somthing went wrong")
    


def update():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="emdb")
        cur=con.cursor()
        sql="update emdb set name='%s',name='%s',post='%s',salary='%s'  where id='%s'"%(id.get(),name.get(),post.get(),salary.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("success","employee records were Updated")
    except:
           messagebox.showerror('Error',"Ooops! Somthing went wrong")
    finally:
        clear()



def delete():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="emdb")
        cur=con.cursor()
        sql= "delete from emdb where id = '%s'"%(id.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("success","employee records has been deleted")
    except:
           messagebox.showerror('Error',"Ooops! Somthing went wrong")






root=Tk()
root.geometry("800x500+400+100")
root.title("Dobbprince Network Employee Management System")
root.configure(bg ="red")
root.resizable(False,False)


#Variables
id=StringVar()
name=StringVar()
post=StringVar()
salary=StringVar()



#ml
#widgets
ml = Label(root, text = "DOBBPRINCE NETWORK MANAGEMENT SYSTEM", bg = "#6C63FF", fg = "white", width=50, font = ("Ariel", 13, "bold"))
ml.place(x = 230, y = 30)


img = PhotoImage(file="EMS.png")
Label(root, image = img, bg= "white").place(x=205, y=70)


frame = Frame(root, width = 400, height = 400, bg ="#a025f9")
frame.place(x = 349, y = 80)

#########################################################


#ID
lbid = Label(root, text="ID", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbid.place(x=390  , y=110)
root.configure(bg ="#A9DFBF")

rgn=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=id)
rgn.place(x=450 , y=110)


#NAME
lbn = Label(root, text="NAME", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbn.place(x=390  , y=150)
root.configure(bg ="#A9DFBF")

rgn=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=name)
rgn.place(x=450 , y=150)


#POST
lbn = Label(root, text="POST", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbn.place(x=390  , y=190)
root.configure(bg ="#A9DFBF")

rgn=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=post)
rgn.place(x=450 , y=190)


#SALARY
lbs = Label(root, text="SALARY", font=("arial",10,"bold"),fg= "Black",bg="#A9DFBF")
lbs.place(x=390  , y=230)
root.configure(bg ="#A9DFBF")

rgn=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=salary)
rgn.place(x=450 , y=230)


#ADDRESS
lbadd = Label(root, text="ADDRESS", font=("arial",10,"bold"),fg= "Black",bg="#A9DFBF")
lbadd.place(x=390  , y=270)
root.configure(bg ="#A9DFBF")

rgn=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable="address")
rgn.place(x=470 , y=270)





#############################################################################################3


#ADD
btnadd = Button(root, text="ADD", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF", command=register)
btnadd.place(x=550 , y=420)

#SEARCH
btns = Button(root, text="SEARCH", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=search)
btns.place(x=610 , y=420)
root.configure(bg ="#A9DFBF")

#UPDATE
btnupd = Button(root, text="UPDATE", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=update)
btnupd.place(x=690 , y=420)

#DELETE
btndel = Button(root, text="DELETE", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=delete)
btndel.place(x=770 , y=420)
root.configure(bg ="#A9DFBF")

#Clear
btnc = Button(root, text="CLEAR", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=clear)
btnc.place(x=860 , y=420)
root.configure(bg ="#A9DFBF")

root.mainloop()


