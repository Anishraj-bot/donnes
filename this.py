from tkinter import *
from tkinter import ttk

class College:
    def __init__(self, raja):
        self.raja = raja
        self.TitleFrame = Frame(self.raja, height=50, width=1200, background="green",bd=2,relief='raised')
        self.TitleFrame.pack()

        self.Title = Label(self.TitleFrame, text="School Management", font="arial 20 bold", width=1200, bg="yellow")
        self.Title.pack()
        self.Frame_1=Frame(self.raja,height=1000,width=300,background="green",bd=2,relief='raised')
        self.Frame_1.pack(side=LEFT)
        self.Frame_1.pack_propagate(0)
        Label(self.Frame_1,text="School details",background="yellow",font="arial 10 bold").place(x=20,y=20)

        self.Id=Label(self.Frame_1,text="Id",background="yellow",font="arial 12 bold")
        self.Id.place(x=30,y=60)
        self.Id_Entry = Entry(self.Frame_1,width=30)
        self.Id_Entry.place(x=90,y=60)
        #======================================
        self.Name=Label(self.Frame_1,text="Name",background="yellow",font="arial 12 bold")
        self.Name.place(x=30,y=90)
        self.Name_Entry = Entry(self.Frame_1,width=30)
        self.Name_Entry.place(x=90,y=90)
        #================================================
        self.Age=Label(self.Frame_1,text="Age",background="yellow",font="arial 12 bold")
        self.Age.place(x=30,y=120)
        self.Age_Entry = Entry(self.Frame_1,width=30)
        self.Age_Entry.place(x=90,y=120)
        #==============================
        self.DOB=Label(self.Frame_1,text="DOB",background="yellow",font="arial 12 bold")
        self.DOB.place(x=20,y=150)
        self.DOB_Entry = Entry(self.Frame_1,width=30)
        self.DOB_Entry.place(x=90,y=150)
        #===================================================
        self.Gender=Label(self.Frame_1,text="Gender",background="yellow",font="arial 12 bold")
        self.Gender.place(x=20,y=180)
        self.Gender_Entry = Entry(self.Frame_1,width=30)
        self.Gender_Entry.place(x=90,y=180)
        #=========================================
        self.City=Label(self.Frame_1,text="City",background="yellow",font="arial 12 bold")
        self.City.place(x=30,y=210)
        self.City_Entry = Entry(self.Frame_1,width=30)
        self.City_Entry.place(x=90,y=210)

        #========================================================
        self.Button_Frame = Frame(self.Frame_1,height=250,width=250,relief="raised",bd=2,background="yellow")
        self.Button_Frame.place(x=30,y=300)
        #========================================
        self.Add=Button(self.Button_Frame,text='Add',width=25,font="arial 11 bold",command=self.Add)
        self.Add.pack()
        #==============================================
        self.Delete=Button(self.Button_Frame,text='Delete',width=25,font="arial 11 bold",command=self.Delete)
        self.Delete.pack()
        #================================================
        self.update=Button(self.Button_Frame,text='update',width=25,font="arial 11 bold",command=self.update)
        self.update.pack()
        #==================================================
        self.clear=Button(self.Button_Frame,text='clear',width=25,font="arial 11 bold",command=self.clear)
        self.clear.pack()
        #====================================================
        
        self.Frame_2= Frame(self.raja,height=1000,width=700,background="green",bd=2,relief='raised')
        self.Frame_2.pack(side=RIGHT)
        self.tree=ttk.Treeview(self.Frame_2,columns=("a1","a2","a3","a4","a5","a6"), show="headings",height=48)
        #=================================================================
        self.tree.column("#1", anchor=CENTER,width=100)
        self.tree.heading("#1",text="ID")
        #==========================================================
        self.tree.column("#2", anchor=CENTER,width=130)
        self.tree.heading("#2",text="Name")
        #================================================
        self.tree.column("#3", anchor=CENTER,width=130)
        self.tree.heading("#3",text="age")
        #=============================================
        self.tree.column("#4", anchor=CENTER,width=120)
        self.tree.heading("#4",text="DOB")
        #=====================================================
        self.tree.column("#5", anchor=CENTER,width=120)
        self.tree.heading("#5",text="Gender")
        #========================================================
        self.tree.column("#6", anchor=CENTER,width=110)
        self.tree.heading("#6",text="city")
        #=======================================================
        self.tree.insert("",index=0,values=(1,"raja",25,"12-12-2022","male","chennai"))
        self.tree.pack()
    def Add(self):
        id = self.Id_Entry.get()
        name = self.Name_Entry.get()
        age = self.Age_Entry.get()
        dob = self.DOB_Entry.get()
        gender = self.Gender_Entry.get()
        city = self.City_Entry.get()
        #==================================
        self.tree.insert("",index=0,values=(id,name,age,dob,gender,city))
    def Delete(self):
        item=self.tree.selection()[0]
        self.tree.delete(item)
    def update(self):
        id = self.Id_Entry.get()
        name = self.Name_Entry.get()
        age = self.Age_Entry.get()
        dob = self.DOB_Entry.get()
        gender = self.Gender_Entry.get()
        city = self.City_Entry.get()
        item = self.tree.selection()[0]
        self.tree.item(item,values=(id,name,age,dob,gender,city))
    def clear(self):
        id = self.Id_Entry.delete(0,END)
        name = self.Name_Entry.delete(0,END)
        age = self.Age_Entry.delete(0,END)
        dob = self.DOB_Entry.delete(0,END)
        gender = self.Gender_Entry.delete(0,END)
        city = self.City_Entry.delete(0,END)
raja = Tk()
raja.title("College Management")
raja.resizable(False, False)
raja.geometry("1000x1000")


College(raja)

raja.mainloop()
