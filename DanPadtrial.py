from tkinter import*
from tkinter import Menu
import webbrowser

#Define function area
def nweb():
    new=2
    url=("https://faforlifebusiness.com/register/DOBBPRINCE")
    webbrowser.open(url,new=new)
    return

root=Tk()
root.title("CashDan notepad Application")
root.geometry("600x600+200+200")

#create the menu bar
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As")
filemenu.add_command(label="Exit")

menubar.add_cascade(label="File",menu=filemenu)
root.config(menu=menubar)

#create the helpmenu
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About us")
helpmenu.add_command(label="Fafolife registration", command=nweb)


menubar.add_cascade(label="Help",menu=helpmenu)


root.config(menu=menubar)

tt=Text(root,state="normal",height=60,width=200)
tt.grid(row=1,column=0,rowspan=12,columnspan=12)


root.mainloop()

