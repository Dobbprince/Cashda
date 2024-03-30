#Design am employee management system of a company

from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


#function area
def clear():
    id.set("")
    name.set("")
    post.set("")
    salary.set("")

def register():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="emdb")
        cur=con.cursor()
        sql="insert into emdb(id,name,post,salary) values('%s','%s','%s','%s',)"%(id.get(),name.get(),post.get(),salary.get())
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
        con=pymysql.connect(host='localhost',user='root',password="",database="politics")
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
root.title("`Dobbprince Network Employee Management System`")
root.configure(bg ="#3f054f")
root.resizable(False,False)


#Variables
id=StringVar()
name=StringVar()
post=StringVar()
salary=StringVar()



#ml
#widgets
ml = Label(root, text = "NIGERIA PRESIDENTIAL ELECTION RESULTS", bg = "#6C63FF", fg = "white", width=40, font = ("Ariel", 15, "bold"))
ml.place(x = 330, y = 30)


img = PhotoImage(file="ElecRes.png")
Label(root, image = img, bg= "white").place(x=205, y=70)


frame = Frame(root, width = 400, height = 400, bg ="#FBF9F9")
frame.place(x = 530, y = 80)
