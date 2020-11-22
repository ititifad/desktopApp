#Frontend

from tkinter import *
import tkinter.messagebox
import stdDatabase_BackEnd

class Student:

    def __init__(self, root):
        self.root =root
        self.root.title("Student Database Management System")
        #self.root.geometry("1350x750+0+0")
        #self.root.state('zoomed')
        self.root.config(bg="cadet blue")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Classroom = StringVar()
        Gender = StringVar()
        Mobile = StringVar()
        School_fees = StringVar()
        Paid_fees = StringVar()
        Remaining_fees = StringVar()
        Status = StringVar()
        Phase = StringVar()
        Date_paid = StringVar()

        #==============================Functions=============================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Database Management Systems", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def ClearData(event=None):
            self.txtStdID.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtsna.delete(0,END)
            self.txtclass.delete(0,END)
            self.txtgender.delete(0,END)
            self.txtmob.delete(0,END)
            self.txtscfee.delete(0,END)
            self.txtpafees.delete(0,END)
            self.txtremfees.delete(0,END)
            self.txtstatus.delete(0,END)
            self.txtphase.delete(0,END)
            self.txtdte.delete(0,END)

        def addData():
            if (len(StdID.get())!=0):
                stdDatabase_BackEnd.addStdRec(StdID.get(), Firstname.get(), Surname.get(), Classroom.get(), Gender.get(), Mobile.get(), \
                                              School_fees.get(), Paid_fees.get(), Remaining_fees.get(), Status.get() ,Phase.get(), Date_paid.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(), Firstname.get(), Surname.get(), Classroom.get(), Gender.get(), Mobile.get(), \
                                             School_fees.get(), Paid_fees.get(), Remaining_fees.get(), Status.get() ,Phase.get(), Date_paid.get()))

        def DisplayData():
            studentlist.delete(0,END)
            for row in stdDatabase_BackEnd.viewData():
                studentlist.insert(END,row,str(""))

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END,sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sd[2])
            self.txtsna.delete(0,END)
            self.txtsna.insert(END,sd[3])
            self.txtclass.delete(0,END)
            self.txtclass.insert(END,sd[4])
            self.txtgender.delete(0,END)
            self.txtgender.insert(END,sd[5])
            self.txtmob.delete(0,END)
            self.txtmob.insert(END,sd[6])
            self.txtscfee.delete(0,END)
            self.txtscfee.insert(END,sd[7])
            self.txtpafees.delete(0,END)
            self.txtpafees.insert(END,sd[8])
            self.txtremfees.delete(0,END)
            self.txtremfees.insert(END,sd[9])
            self.txtstatus.delete(0,END)
            self.txtstatus.insert(END,sd[10])
            self.txtphase.delete(0,END)
            self.txtphase.insert(END,sd[11])
            self.txtdte.delete(0,END)
            self.txtdte.insert(END,sd[12])

        def DeleteDate():
            if(len(StdID.get())!=0):
                stdDatabase_BackEnd.deleteRec(sd[0])
                ClearData()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0,END)
            for row in stdDatabase_BackEnd.searchData(StdID.get(), Firstname.get(), Surname.get(), Classroom.get(), Gender.get(), Mobile.get(), \
                                                      School_fees.get(), Paid_fees.get(), Remaining_fees.get(), Status.get(), Phase.get(), Date_paid.get()):
                studentlist.insert(END,row,str(""))

        def update():
            if(len(StdID.get())!=0):
                stdDatabase_BackEnd.deleteRec(sd[0])
            if(len(StdID.get())!=0):
                stdDatabase_BackEnd.addStdRec(StdID.get(), Firstname.get(), Surname.get(), Classroom.get(), Gender.get(), Mobile.get(), School_fees.get(), Paid_fees.get(), Remaining_fees.get(), Status.get(), Phase.get(), Date_paid.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(), Firstname.get(), Surname.get(), Classroom.get(), Gender.get(), Mobile.get(), School_fees.get(), Paid_fees.get(),Remaining_fees.get(), Status.get(), Phase.get(), Date_paid.get()))
                
        #=============================Frames===============================
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=8, padx=54, pady=8, bg="ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 40,'bold'),text="Student Database Management Systems", bg="Ghost White")
        self.lblTit.grid(padx=2)

        ButtonFrame = Frame(MainFrame, bd=8, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=8, width=120, height=400, padx=20, pady=20, bg="Ghost White", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=8, width=1000, height=600, padx=20, bg="Ghost White", relief=RIDGE,
                              font=('arial', 20,'bold'),text="Student Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=8, width=450, height=200, padx=31, pady=3, bg="Ghost White", relief=RIDGE,
                                    font=('arial', 20,'bold'),text="Student Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        #====================================================labels and Entry Widget================================
        self.lblStdID = Label(DataFrameLEFT, font=('arial', 20,'bold'),text="Student ID:", padx=2, pady=2, bg="Ghost White")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font=('arial', 20,'bold'), textvariable=StdID, width=20)
        self.txtStdID .grid(row=0, column=1)
        
        self.lblfna = Label(DataFrameLEFT, font=('arial', 20,'bold'),text="Firstname:", padx=2, pady=2, bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('arial', 20,'bold'), textvariable=Firstname, width=20)
        self.txtfna .grid(row=1, column=1)
        
        self.lblsna = Label(DataFrameLEFT, font=('arial', 20,'bold'),text="Surname:", padx=2, pady=2, bg="Ghost White")
        self.lblsna.grid(row=2, column=0, sticky=W)
        self.txtsna = Entry(DataFrameLEFT, font=('arial', 20,'bold'), textvariable=Surname, width=20)
        self.txtsna .grid(row=2, column=1)
        
        self.lblclass = Label(DataFrameLEFT, font=('arial', 20,'bold'),text="Classroom:", padx=2, pady=2, bg="Ghost White")
        self.lblclass.grid(row=3, column=0, sticky=W)
        self.txtclass = Entry(DataFrameLEFT, font=('arial', 20,'bold'), textvariable=Classroom, width=20)
        self.txtclass .grid(row=3, column=1)

        self.lblgender = Label(DataFrameLEFT, font=('arial', 20,'bold'),text="Gender:", padx=2, pady=2, bg="Ghost White")
        self.lblgender.grid(row=4, column=0, sticky=W)
        self.txtgender = Entry(DataFrameLEFT, font=('arial', 20,'bold'), textvariable=Gender, width=20)
        self.txtgender .grid(row=4, column=1)
        
        self.lblmob = Label(DataFrameLEFT, font=('arial', 20,'bold'),text="Mobile:", padx=2, pady=2, bd=4, bg="Ghost White")
        self.lblmob.grid(row=5, column=0, sticky=W)
        self.txtmob = Entry(DataFrameLEFT, font=('arial', 20,'bold'), textvariable=Mobile, width=20)
        self.txtmob .grid(row=5, column=1)

        self.lblscfee = Label(DataFrameLEFT, font=('arial', 20,'bold'),text="School Fees:", padx=2, pady=2, bg="Ghost White")
        self.lblscfee.grid(row=6, column=0, sticky=W)
        self.txtscfee = Entry(DataFrameLEFT, font=('arial', 20,'bold'), textvariable=School_fees, width=20)
        self.txtscfee .grid(row=6, column=1)

        self.lblpafees = Label(DataFrameLEFT, font=('arial', 20,'bold'),text="Paid Fees:", padx=2, pady=2, bg="Ghost White")
        self.lblpafees.grid(row=7, column=0, sticky=W)
        self.txtpafees = Entry(DataFrameLEFT, font=('arial', 20,'bold'), textvariable=Paid_fees, width=20)
        self.txtpafees .grid(row=7, column=1)

        self.lblremfees = Label(DataFrameLEFT, font=('arial', 20,'bold'),text="Remaining:", padx=2, pady=2, bg="Ghost White")
        self.lblremfees.grid(row=8, column=0, sticky=W)
        self.txtremfees = Entry(DataFrameLEFT, font=('arial', 20,'bold'), textvariable=Remaining_fees, width=20)
        self.txtremfees .grid(row=8, column=1)

        self.lblstatus = Label(DataFrameLEFT, font=('arial', 20,'bold'),text="Status:", padx=2, pady=2, bg="Ghost White")
        self.lblstatus.grid(row=9, column=0, sticky=W)
        self.txtstatus = Entry(DataFrameLEFT, font=('arial', 20,'bold'), textvariable=Status, width=20)
        self.txtstatus .grid(row=9, column=1)

        self.lblphase = Label(DataFrameLEFT, font=('arial', 20,'bold'),text="Phase:", padx=2, pady=2, bg="Ghost White")
        self.lblphase.grid(row=10, column=0, sticky=W)
        self.txtphase = Entry(DataFrameLEFT, font=('arial', 20,'bold'), textvariable=Phase, width=20)
        self.txtphase .grid(row=10, column=1)

        self.lbldte = Label(DataFrameLEFT, font=('arial', 20,'bold'),text="Date Paid", padx=2, pady=2, bg="Ghost White")
        self.lbldte.grid(row=11, column=0, sticky=W)
        self.txtdte = Entry(DataFrameLEFT, font=('arial', 20,'bold'), textvariable=Date_paid, width=20)
        self.txtdte .grid(row=11, column=1)

        #=======================================================listbox and scrollbar================================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width=41, height=16,  font=('arial', 12,'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = studentlist.yview)

        #====================================================Button Widget========================================

        self.btnAddDate = Button(ButtonFrame, text="Add new", font=('arial', 20,'bold'),height=1, width=10, command=addData)
        self.btnAddDate.grid(row=0, column=0)

        self.btnDisplay = Button(ButtonFrame, text="Display", font=('arial', 20,'bold'),height=1, width=10,command=DisplayData)
        self.btnDisplay.grid(row=0, column=1)

        self.btnClear = Button(ButtonFrame, text="Clear", font=('arial', 20,'bold'),height=1, width=10,command=ClearData)
        self.btnClear.grid(row=0, column=2)

        self.btnDelete = Button(ButtonFrame, text="Delete", font=('arial', 20,'bold'),height=1, width=10,command=DeleteDate)
        self.btnDelete.grid(row=0, column=3)

        self.btnSearch = Button(ButtonFrame, text="Search", font=('arial', 20,'bold'),height=1, width=10,command=searchDatabase)
        self.btnSearch.grid(row=0, column=4)

        self.btnUpdate = Button(ButtonFrame, text="Update", font=('arial', 20,'bold'),height=1, width=10,command=update)
        self.btnUpdate.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 20,'bold'),height=1, width=10,command=iExit)
        self.btnExit.grid(row=0, column=6)










        

if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.attributes('-fullscreen', True)
    root.bind("<F11>", lambda event: root.attributes("-fullscreen",
              not root.attributes("-fullscreen")))
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
    root.mainloop()
    
