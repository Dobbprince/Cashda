from tkinter import *

from tkinter import messagebox

#function area
def register():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="rtisdb")
        cur=con.cursor()
        sql="insert into students values('%s','%s','%s','%s','%s')"%(matno.get(),fname.get(),lname.get(),uname.get(),gender.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("success","congrats! Registration record was saved")
    except:
           messagebox.showerror('Error',"Ooops! Somthing went rong")
    




root=Tk()
root.geometry("1300x600+200+200")
root.title("SIGN UP FORM")
root.configure(bg ="orange")
root.resizable(False,False)



#Variables
matno=StringVar()
fname=StringVar()
lname=StringVar()
uname=StringVar()
gender=StringVar()

#ml
#widgets
ml = Label(root, text = "SIGN UP FORM", bg = "#6C63FF", fg = "white", width=30, font = ("Ariel", 15, "bold"))
ml.place(x = 330, y = 30)




frame = Frame(root, width = 400, height = 400, bg ="#FBF9F9")
frame.place(x = 530, y = 80)

####################################################

#MATRICULATION NO
lbrgn = Label(root, text="MAT NO", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbrgn.place(x=550  , y=120)
root.configure(bg ="#A9DFBF")

rgn=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=matno)
rgn.place(x=650 , y=120)

#FIRST NAME
lbfn = Label(root, text="FN", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbfn.place(x=550 , y=165)
root.configure(bg ="#A9DFBF")

fn=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=fname)
fn.place(x=650 , y=165)

#LAST NAME
lbln = Label(root, text="LN", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbln.place(x=550 , y=210)
root.configure(bg ="#A9DFBF")

ln=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=lname)
ln.place(x=650 , y=210)

#USERNAME
lbun = Label(root, text="USERNAME", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbun.place(x=550 , y=250)
root.configure(bg ="#A9DFBF")

un=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=uname)
un.place(x=650 , y=250)

#GENDER
lbgen = Label(root, text="GENDER", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbgen.place(x=550 , y=290)
root.configure(bg ="#A9DFBF")

pd=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),show='*',textvariable=gender)
pd.place(x=650 , y=290)





#Register
btnreg = Button(root, text="register", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF", command=register)
btnreg.place(x=545 , y=320)




