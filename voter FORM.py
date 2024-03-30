from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

def clear():
    regno.set("")
    vin.set("")
    delim.set("")
    fnames.set("")
    dob.set("")
    gen.set("")
    occu.set("")
    addr.set("")

def add():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="NIGERIA ELECTORAL VALIDATION FORM")
        cur=con.cursor()
        sql="insert into voter values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(regno.get(),vin.get(),delim.get(),fnames.get(),dob.get(),gen.get(),occu.get(),addr.get()) #dob.get(),dob.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("success","congrats! you have now been validated to cast your vote")
    except:
           messagenbox.showerror('Error',"Ooops! Somthing went rong, try again please.")
    finally:
           clear()

def search():
        try:
            con=pymysql.connect(host='localhost',user='root',password="",database="NIGERIA ELECTORAL VALIDATION FORM")
            cur=con.cursor()
            sql="select * from voters where regno='%s'"%regno.get() 
            cur.execute(sql)
            result=cur.fetchone()
            regno.set(result[1])
            vin.set(result[2])
            delim.set(result[3])
            fnames.set(result[4])
            dob.set(result[5])
            gen.set(result[6])
            occu.set(result[7])
            addr.set(result[8])
            con.close()
        except:
             messagebox.showerror('Error',"Ooops! Somthing went rong")

def update():
        try:
            con=pymysql.connect(host='localhost',user='root',password="",database="NIGERIA ELECTORAL VALIDATION FORM")
            cur=con.cursor()
            sql="update voters set code='%s',vin='%s',delim='%s',fnames='%s',dob='%s',gen='%s',occu='%s',addr='%s'  where regno='%s'"%(code.get(),vin.get(),delim.get(),fnames.get(),dob.get(),gen.get(),occu.get(),addr.get())
        
            cur.execute(sql)
            con.commit()
            con.close()
            messagebox.showinfo("success","congrats! your record was saved")
        except:
            messagebox.showerror('Error',"Ooops! Somthing went rong")
        finally:
            clear()

def delete():
        try:
            con=pymysql.connect(host='localhost',user='root',password="",database="NIGERIA ELECTORAL VALIDATION FORM")
            cur=con.cursor()
            sql="delete from voters where '$'"%(regno.get())
            cur.execute(sql)
            con.commit()
            con.close()
            messagebox.showinfo("success","congrats! your record was saved")
        except:
            messagebox.showerror('Error',"Ooops! Somthing went rong")
        finally:
            clear()
  
win = Tk()
win.geometry("750x900+200+200")
win.title("NIGERIA ELECTORAL VALIDATION FORM")
win.configure(bg ="#21F1BF")
win.resizable(False,False)

#Variables
regno=StringVar()
vin=StringVar()
delim=StringVar()
nov=StringVar()
dob=StringVar()
gen=StringVar()
occu=StringVar()
addr=StringVar()



#widgets
ml = Label(win, text = "SIGN UP FORM", bg = "#6C63FF", fg = "white", width=30, font = ("Ariel", 15, "bold"))
ml.place(x = 330, y = 30)


img = PhotoImage(file="Vote 1")
Label(win, image = img, bg= "white").place(x=285, y=70)


frame = Frame(win, width = 400, height = 400, bg ="#FBF9F9")
frame.place(x = 530, y = 80)



#add widgets
lbl = Label(win, text="Validation Form For Election", font=('arial',15,'bold'),fg= 'blue',bg='#A9DFBF' )
#lbl.grid(row=3 , column=0)
#lbl.pack()
lbl.place(x=250 , y=25)


#add widgets
lbl = Label(win, text="VOTERS FORM", font=('arial',18,'bold'),fg= 'GREEN',bg='#A9DFBF' )
#lbl.grid(row=2 , column=0)
#lbl.pack()
lbl.place(x=270 , y=55)


#SELECT YOUR PREFERED CANDIDATE
sub= Checkbutton(win, text="Select your prefered candidate", bg='#A9DFBF')
sub.place(x=70 , y=290)


state = ttk.Combobox(win, state='readonly', width=35)
state['value']=('select a state', 'FCT Abuja', 'Abia', 'Adamawa', "Awkwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno",'Cross River','Delta',"Ebonyi","Edo","Ekiti","Enugu","Gombe","Imo","Jigawa","Kaduna","Kano","Katsina","Kebbi","Kogi","Kwara","Lagos","Nasarawa","Niger","Ogun","Ondo","Osun","Oyo","Plateau","Rivers","Sokoto","Taraba","Yobe","Zamfara")
state.current(0)
state.place(x=70, y=236)


cd= Listbox(win)
cd.insert(1,"Peter Obi")
cd.insert(2,"Atiku Abubakar")
cd.insert(3,"Bola Tinubu")
cd.insert(4,"Rabiu Musa kwakwaso")
cd.insert(5,"Showore Omoyele")
cd.insert(6,"kola Abiola")
cd.insert(7,"Hamza")
cd.insert(8,"Christopher Imumule")
cd.insert(9,"Dumebi Kachikwu")
cd.insert(10,"Peter Umeadi")
cd.insert(10,'okwudili Anyajike')
cd.place(x=70 , y=320)

radbtn= Radiobutton(win, text= "Male", value=1,bg='#A9DFBF')
radbtn.place(x= 70 , y=490)
radbtn= Radiobutton(win, text= "FeMale", value=2,bg='#A9DFBF')
radbtn.place(x= 130 , y=490)


#REGISTRATION NUMBER
btn = Button(win, text="REGNO", font=("arial",12,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=70 , y=190)
win.configure(bg ="#A9DFBF")

regno=Entry(win, width=12, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=regno)
regno.place(x=150 , y=190)

#VIN
btn = Button(win, text="VIN", font=("arial",12,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=260 , y=105)
win.configure(bg ="#A9DFBF")

vin=Entry(win, width=21, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=vin)
vin.place(x=305 , y=105)

#DELIM
btn = Button(win, text="DELIM", font=("arial",12,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=503 , y=100)
win.configure(bg ="#A9DFBF")

delim=Entry(win, width=19, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=delim)
delim.place(x=568 , y=100)

#NAME OF VOTER
btn = Button(win, text="NAME OF VOTER", font=("arial",12,"bold"),fg= "red",bg="blue")
btn.place(x=107 , y=100)

display=Entry(win, width=25, fg='blue',bg='orange',font=('arial',12,'bold'),textvariable=NO)
display.place(x=70 , y=150)

#DATEOFBIRTH
btn = Button(win, text="DATE OF BIRTH", font=("arial",10,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=307 , y=150)
win.configure(bg ="#A9DFBF")

dob=Entry(win, width=12, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=dob)
dob.place(x=422 , y=150)


#GEN
btn = Button(win, text="GENDER", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=540 , y=150)
win.configure(bg ="#A9DFBF")

gen=Entry(win, width=11, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=gen)
gen.place(x=630 , y=150)


#OCCUPATION
btn = Button(win, text="OCCUPATION", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=290 , y=190)
win.configure(bg ="#A9DFBF")

occu=Entry(win, width=11, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=occu)
occu.place(x=410 , y=190)


#ADDRESS
btn = Button(win, text="ADDRESS", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
btn.place(x=520 , y=190)
win.configure(bg ="#A9DFBF")

addr=Entry(win, width=13, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=addr)
addr.place(x=620 , y=190)















#SUBMIT
btna = Button(win, text="SUBMIT", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=sub)
btna.place(x=50 , y=590)

#SEARCH
btns = Button(win, text="SEARCH", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=search)
btns.place(x=130 , y=590)
win.configure(bg ="#A9DFBF")

#UPDATE
btnu = Button(win, text="UPDATE", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=update)
btnu.place(x=220 , y=590)

#DELETE
btnd = Button(win, text="DELETE", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=delete)
btnd.place(x=310 , y=590)
win.configure(bg ="#A9DFBF")


#Clear
btnc = Button(win, text="CLEAR", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=clear)
btnc.place(x=390 , y=590)
win.configure(bg ="#A9DFBF")









win.mainloop()

