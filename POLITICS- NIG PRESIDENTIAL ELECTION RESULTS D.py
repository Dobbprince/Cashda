
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


#function area
def clear():
    cname.set("")
    anrp.set("")
    accord.set("")
    pdp.set("")
    nnpp.set("")
    lp.set("")
    aa.set("")
    adp.set("")
    apc.set("")

def register():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="politics")
        cur=con.cursor()
        sql="insert into politics(uid,cname,anrp,accord,pdp,nnpp,lp,aa,adp,apc) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(uid.get(),cname.get(),anrp.get(),accord.get(),pdp.get(),nnpp.get(),lp.get(),aa.get(),adp.get(),apc.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("success","congrats!Nig presidential election results were saved")
    except:
           messagebox.showerror('Error',"Ooops! Somthing went wrong")
    

def search():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="politics")
        cur=con.cursor()
        sql="select * from politics where uid='%s'"%uid.get()
        cur.execute(sql)
        result=cur.fetchone()
        cname.set(result[1])
        anrp.set(result[2])
        accord.set(result[3])
        pdp.set(result[4])
        nnpp.set(result[5])
        lp.set(result[6])
        aa.set(result[7])
        adp.set(result[8])
        apc.set(result[9])
        con.close()
        messagebox.showinfo("success","congrats!These is the election search results")
    except:
           messagebox.showerror('Error',"Ooops! Somthing went wrong")
    


def update():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="politics")
        cur=con.cursor()
        sql="update politics set cname='%s',anrp='%s',accord='%s',pdp='%s',nnpp='%s',lp='%s',aa='%s',adp='%s',apc='%s'  where uid='%s'"%(cname.get(),anrp.get(),accord.get(),pdp.get(),nnpp.get(),lp.get(),aa.get(),adp.get(),apc.get,uid.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("success","congrats!Nig presidential election results were Updated")
    except:
           messagebox.showerror('Error',"Ooops! Somthing went wrong")
    finally:
        clear()



def delete():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="politics")
        cur=con.cursor()
        sql= "delete from politics where uid = '%s'"%(uid.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("success","congrats!Nig presidential election results has been deleted")
    except:
           messagebox.showerror('Error',"Ooops! Somthing went wrong")


win=Tk()
win.geometry("1300x600+200+200")
win.title("Nigeria Presidential Election Results")
win.configure(bg ="#07E4AF")
win.resizable(False,False)



#Variables
uid=StringVar()
cname=StringVar()
anrp=StringVar()
accord=StringVar()
pdp=StringVar()
nnpp=StringVar()
lp=StringVar()
aa=StringVar()
adp=StringVar()
apc=StringVar()



#ml
#widgets
ml = Label(win, text = "NIGERIA PRESIDENTIAL ELECTION RESULTS", bg = "#6C63FF", fg = "white", width=40, font = ("Ariel", 15, "bold"))
ml.place(x = 330, y = 30)


img = PhotoImage(file="")
Label(win, image = img, bg= "white").place(x=205, y=70)


frame = Frame(win, width = 400, height = 400, bg ="#FBF9F9")
frame.place(x = 530, y = 80)

####################################################

#USER ID
lbuid = Label(win, text="UID", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbuid.place(x=550  , y=120)
win.configure(bg ="#A9DFBF")

rgn=Entry(win, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=uid)
rgn.place(x=650 , y=120)

#CANDIDATE NAME
lbcn = Label(win, text="Cand Name", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbcn.place(x=550 , y=150)
win.configure(bg ="#A9DFBF")

cn=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=cname)
cn.place(x=650 , y=150)

#ANRP
lbANRP = Label(root, text="ANRP", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbANRP.place(x=550 , y=178)
win.configure(bg ="#A9DFBF")

ln=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=anrp)
ln.place(x=650 , y=178)

#ACCORD
lba = Label(root, text="ACCORD", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lba.place(x=550 , y=208)
win.configure(bg ="#A9DFBF")

un=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=accord)
un.place(x=650 , y=208)


#PDP
lbpdp = Label(root, text="PDP", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbpdp.place(x=550 , y=235)
win.configure(bg ="#A9DFBF")

un=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=pdp)
un.place(x=650 , y=235)


#NNPP
lbnnpp = Label(root, text="NNPP", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbnnpp.place(x=550 , y=265)
win.configure(bg ="#A9DFBF")

un=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=nnpp)
un.place(x=650 , y=265)


#Labour Party
lblp = Label(root, text="Labour Party", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lblp.place(x=550 , y=295)
win.configure(bg ="#A9DFBF")

un=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=lp)
un.place(x=650 , y=295)


#Action Alliance
lbaa = Label(root, text="AA", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbaa.place(x=550 , y=325)
win.configure(bg ="#A9DFBF")

un=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=aa)
un.place(x=650 , y=325)


#Action Democratic Party
lbaa = Label(root, text="ADP", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbaa.place(x=550 , y=352)
win.configure(bg ="#A9DFBF")

un=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=adp)
un.place(x=650 , y=352)


#All Progressives Congress
lbapc = Label(root, text="APC", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbapc.place(x=550 , y=382)
win.configure(bg ="#A9DFBF")

un=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=apc)
un.place(x=650 , y=382)








#SUBMIT
btnadd = Button(root, text="ADD", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF", command=register)
btnadd.place(x=550 , y=420)

#SEARCH
btns = Button(root, text="SEARCH", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=search)
btns.place(x=610 , y=420)
win.configure(bg ="#A9DFBF")

#UPDATE
btnupd = Button(root, text="UPDATE", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=update)
btnupd.place(x=690 , y=420)

#DELETE
btndel = Button(root, text="DELETE", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=delete)
btndel.place(x=770 , y=420)
win.configure(bg ="#A9DFBF")

#Clear
btnc = Button(root, text="CLEAR", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=clear)
btnc.place(x=860 , y=420)
win.configure(bg ="#A9DFBF")

root.mainloop()
