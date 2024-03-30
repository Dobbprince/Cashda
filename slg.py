from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

#function area

#function area
def clear():
    gender.set("")
    WhoDoYouReportTo("")
    WhatDepartmentAreYouIn.set("")
    HowLongHaveYouBeenWorkingHere.set("")
    WhatDoYouLikeMostAboutWorkingHere.set("")
    HowWouldYouDescribeTheWorkEnvironment/ethic.set("")
    UponEmployment,WereYouProperlyOn-boarded.set("")
    WhatMediumOfCommunicationIsUsedHere.set("")
    DoYouFeelYourDepartment/LineManagersMotivateTheTeam.set("")
    HowWouldYouDescribeTheLevelOfSupportOffered.set("")
    HowDoStaffReceiveFeedback.set("")
    IsYourCareerGrowthPlanClearHere.set("")
    WhatWouldMakeYourWorkMoreProductive.set("")
    WhenPeopleMakeMistakesHere,HowIsItHandled.set("")


        
def register():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="JEC Questionnaires")
        cur=con.cursor()
        sql="insert into staff values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(gender.get(),WhoDoYouReportTo.get(),WhatDepartmentAreYouIn.get(),HowLongHaveYouBeenWorkingHere.get(),WhatDoYouLikeMostAboutWorkingHere.get(),HowWouldYouDescribeTheWorkEnvironment/ethic.get(),UponEmployment,WereYouProperlyOn-boarded.get(),WhatMediumOfCommunicationIsUsedHere.get(),DoYouFeelYourDepartment/LineManagersMotivateTheTeam.get(),HowWouldYouDescribeTheLevelOfSupportOffered.get(),HowDoStaffReceiveFeedback.get(),IsYourCareerGrowthPlanClearHere.get(),WhatWouldMakeYourWorkMoreProductive.get(),WhenPeopleMakeMistakesHere,HowIsItHandled.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("success","congrats! Registration record was saved")
    except:
           messagebox.showerror('Error',"Ooops! Somthing went rong")


def update():
    try:
        con=pymysql.connect(host='localhost',user='root',password="",database="JEC Questionnaires")
        cur=con.cursor()
        sql="update staff set gender='%s',WhoDoYouReportTo='%s',WhatDepartmentAreYouIn='%s',HowLongHaveYouBeenWorkingHere='%s',WhatDoYouLikeMostAboutWorkingHere='%s',HowWouldYouDescribeTheWorkEnvironment/ethic='%s',UponEmployment,WereYouProperlyOn-boarded='%s',WhatMediumOfCommunicationIsUsedHere='%s',DoYouFeelYourDepartment/LineManagersMotivateTheTeam='%s',HowWouldYouDescribeTheLevelOfSupportOffered='%s',HowDoStaffReceiveFeedback='%s',IsYourCareerGrowthPlanClearHere='%s',WhatWouldMakeYourWorkMoreProductive='%s',WhenPeopleMakeMistakesHere,HowIsItHandled='%s'where matno='%s'"%(gender.get(),WhoDoYouReportTo.get(),WhatDepartmentAreYouIn.get(),HowLongHaveYouBeenWorkingHere.get(),WhatDoYouLikeMostAboutWorkingHere.get(),HowWouldYouDescribeTheWorkEnvironment/ethic.get(),UponEmployment,WereYouProperlyOn-boarded.get(),WhatMediumOfCommunicationIsUsedHere.get(),DoYouFeelYourDepartment/LineManagersMotivateTheTeam.get(),HowWouldYouDescribeTheLevelOfSupportOffered.get(),HowDoStaffReceiveFeedback.get(),IsYourCareerGrowthPlanClearHere.get(),WhatWouldMakeYourWorkMoreProductive.get(),WhenPeopleMakeMistakesHere,HowIsItHandled.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("success","Your Information is/has been Updated")
    except:
           messagebox.showerror('Error',"Ooops! Somthing went wrong")
    finally:
        clear()



root=Tk()
root.geometry("1500x720+70+70")
root.title("JEC Questionnaires")
root.configure(bg ="#FFA500")
root.resizable(False,False)



#Variables
gender=StringVar()
WhoDoYouReportTo=StringVar()
WhatDepartmentAreYouIn=StringVar()
HowLongHaveYouBeenWorkingHere=StringVar()
WhatDoYouLikeMostAboutWorkingHere=StringVar()
HowWouldYouDescribeTheWorkEnvironmentEthic=StringVar()
uponEmploymentWereYouProperlyOnboarded=StringVar()
WhatMediumOfCommunicationIsUsedHere=StringVar()
doYouFeelYourDepartmentLineManagersMotivateTheTeam=StringVar()
HowWouldYouDescribeTheLevelOfSupportOffered=StringVar()
HowDoStaffReceiveFeedback=StringVar()
IsYourCareerGrowthPlanClearHere=StringVar()
WhatWouldMakeYourWorkMoreProductive=StringVar()
WhenPeopleMakeMistakesHereHowIsItHandled=StringVar()

#ml
#widgets
ml = Label(root, text = "JEC Questionnaires", bg = "#FF00FF", fg = "green", width=50, font = ("Ariel", 16, "bold"))
ml.place(x = 430, y = 30)


img = PhotoImage(file="")
Label(root, image = img, bg= "white").place(x=105, y=70)

#X GOES > LEFT
frame = Frame(root, width = 1360, height = 550, bg ="#008000")
frame.place(x = 120, y = 100)


####################################################

#SEX
lbgen = Label(root, text="SEX", font=("arial",14,"bold"),fg= "Black",bg="#A9DFBF")
lbgen.place(x=150  , y=120)
root.configure(bg ="#A9DFBF")

radbtn = Radiobutton(root, text= "MALE", value=1,bg='#A9DFBF')
radbtn.place(x= 250 , y=120)

radbtn = Radiobutton(root, text= "FEMALE", value=2,bg='#A9DFBF')
radbtn.place(x= 370 , y=120)




#WHATDEPARTMENTAREYOU IN
lbdep = Label(root, text="What Department Are You In", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbdep.place(x=150 , y=210)
root.configure(bg ="#A9DFBF")


ln=Entry(root, width=20, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=WhatDepartmentAreYouIn)
ln.place(x=370 , y=210)



#WHO DO YOU REPORT TO
lbwk = Label(root, text="Who Do You Report To", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbwk.place(x=150 , y=250)
root.configure(bg ="#A9DFBF")

un=Entry(root, width=10, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=WhoDoYouReportTo)
entry= Entry(root)

entry.pack()
un.place(x=370 , y=250)


#HOWLONGHAVEYOUBEENWORKINGHERE
lbwk = Label(root, text="How Long Have You Been Working Here", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbwk.place(x=150 , y=295)
root.configure(bg ="#A9DFBF")


combobox= ttk.Combobox(root,state= "readonly")
combobox['values']=("3 - 6 MONTHS","1 - 2 YEARS","3 - 5 YEARS")
combobox.current(2)
combobox.pack(pady=280, ipadx=150)




#WHAT DO YOU LIKE MOST ABOUT WORKING HERE
lbgen = Label(root, text="What Do You Like Most About Working Here", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbgen.place(x=150 , y=330)
root.configure(bg ="#A9DFBF")

pd=Entry(root, width=30, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=gender)
pd.place(x=490 , y=330)

#HOW WOULD YOU DESCRIBE THE WORK ENVIRONMENT/ETHIC
lbwk = Label(root, text="How Would You Describe The Work Environment/Ethic", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbwk.place(x=150 , y=370)
root.configure(bg ="#A9DFBF")

un=Entry(root, width=30, fg='Black',bg='#CDE6E0',font=('arial',13,'bold'),textvariable=HowWouldYouDescribeTheWorkEnvironmentEthic)
un.place(x=550 , y=370)

#UPON EMPLOYMENT, WHERE YOU PROPERLY ON-BOARDED
lbwk = Label(root, text="Upon Employment, Were You Properly On-boarded", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbwk.place(x=150 , y=600)
root.configure(bg ="#A9DFBF")

combobox= ttk.Combobox(root,state= "readonly")
combobox['values']=("YES","NO")
combobox.current(1)
combobox.pack(pady=0, ipadx=150)


#WHAT MEDIUM OF COMMUNICATION IS USED HERE
lbmc = Label(root, text="What Medium Of Communication Is Used Here", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbmc.place(x=150 , y=450)
root.configure(bg ="#A9DFBF")

radbtn= Radiobutton(root, text= "PHONE", value=1,bg='#A9DFBF')
radbtn.place(x= 550 , y=450)
radbtn= Radiobutton(root, text= "EMAIL", value=2,bg='#A9DFBF')
radbtn.place(x= 660 , y=450)
radbtn= Radiobutton(root, text= "PHYSICAL/VIRTUAL", value=3,bg='#A9DFBF')
radbtn.place(x= 760 , y=450)

#DO YOU FEEL YOUR DEPARTMENT LINE MANAGERS MOTIVATE THE TEAM
lbmc = Label(root, text="Do You Feel Your Department Line Managers Motivate The Team", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbmc.place(x=150 , y=490)
root.configure(bg ="#A9DFBF")

radbtn= Radiobutton(root, text= "YES", value=1,bg='#A9DFBF')
radbtn.place(x= 660 , y=490)
radbtn= Radiobutton(root, text= "NO", value=2,bg='#A9DFBF')
radbtn.place(x= 760 , y=490)

#HOW WOULD YOU DESCRIBE THE LEVEL OF SUPPORT OFFERED
lbmc = Label(root, text="How Would You Describe The Level Of Support Offered", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbmc.place(x=150 , y=530)
root.configure(bg ="#A9DFBF")

radbtn= Radiobutton(root, text= "Satisfactory( Meetings expectations)", value=0,bg='#A9DFBF')
radbtn.place(x= 570 , y=530)
radbtn= Radiobutton(root, text= "Unsatisfactory(Below expectations)", value=1,bg='#A9DFBF')
radbtn.place(x= 800 , y=530)
radbtn= Radiobutton(root, text= "Excellent(Exceedind expectations)", value=2,bg='#A9DFBF')
radbtn.place(x= 1025 , y=530)


#HOW DO STAFF RECEIVE FEEDBACK
lbmc = Label(root, text="How do Staff receive feedback?", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbmc.place(x=150 , y=530)
root.configure(bg ="#A9DFBF")

radbtn= Radiobutton(root, text= "Satisfactory( Meetings expectations)", value=1,bg='#A9DFBF')
radbtn.place(x= 570 , y=530)
radbtn= Radiobutton(root, text= "Unsatisfactory(Below expectations)", value=2,bg='#A9DFBF')
radbtn.place(x= 800 , y=530)
radbtn= Radiobutton(root, text= "Excellent(Exceedind expectations)", value=3,bg='#A9DFBF')
radbtn.place(x= 1025 , y=530)


#Is your career growth plan clear here?
lbwk = Label(root, text="Is your career growth plan clear here?", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF")
lbwk.place(x=150 , y=570)
root.configure(bg ="#A9DFBF")

radbtn= Radiobutton(root, text= "YES", value=0,bg='#A9DFBF')
radbtn.place(x= 490 , y=570)
radbtn= Radiobutton(root, text= "NO", value=1,bg='#A9DFBF')
radbtn.place(x= 570 , y=570)




#REGISTER
btnreg = Button(root, text="submit", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF", command=register)
btnreg.place(x=545 , y=320)


#UPDATE
btnupd = Button(root, text="UPDATE", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=update)
btnupd.place(x=690 , y=420)


#Clear
btnc = Button(root, text="CLEAR", font=("arial",11,"bold"),fg= "Black",bg="#A9DFBF",command=clear)
btnc.place(x=860 , y=420)
root.configure(bg ="#A9DFBF")


root.mainloop()

