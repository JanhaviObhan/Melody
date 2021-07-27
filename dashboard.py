from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
from record import recordclass
from newartist import newartistclass
from about import aboutclass
class Melody:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Melody - Music Album Management System   |   Janhavi Obhan SE-IT-40")
        self.root.config(bg="#e0cee0")

        self.icon_title=PhotoImage(file="images/icon.png")
        title=Label(self.root, text="Melody - Music Album Management System",image=self.icon_title,compound=LEFT,font=("broadway",38,"bold"),bg="#9663c4",fg="#5d5b6a",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        self.lbl_clock=Label(self.root, text="Welcome to Melody, find a well organized list of all your music in one place!",font=("cambria",15),bg="#c6aadb",fg="#5d5b6a")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=35)

        self.MenuLogo1=Image.open("images/menulogo1.jpg")
        self.MenuLogo1=self.MenuLogo1.resize((185,185),Image.ANTIALIAS)
        self.MenuLogo1=ImageTk.PhotoImage(self.MenuLogo1)

        LeftMenu=Frame(self.root, bd=2, relief=RIDGE,bg="#fcecdc")
        LeftMenu.place(x=0,y=105,width=200,height=594)

        lbl_menulogo=Label(LeftMenu, image=self.MenuLogo1)
        lbl_menulogo.pack(side=TOP, fill=X)

        lbl_view=Label(LeftMenu,text="Main Menu",font=("cambria",15),bg="#E2C3C8").pack(side=TOP,fill=X)
        btn_albums=Button(LeftMenu,text="View/Update\nYour\nRecords",command=self.record,font=("cambria",12,"bold"),bg="#779ecb",bd=3,relief=GROOVE,cursor="hand2").pack(side=TOP,fill=X)
        btn_artists=Button(LeftMenu,text="Add\nNew\nArtist",command=self.newartist,font=("cambria",12,"bold"),bg="#92b9e7",bd=3,relief=GROOVE,cursor="hand2").pack(side=TOP,fill=X)
        btn_genres=Button(LeftMenu,text="About",command=self.about,font=("cambria",12,"bold"),bg="#caf1ff",bd=3,relief=GROOVE,cursor="hand2").pack(side=TOP,fill=X)

        self.MenuLogo2=Image.open("images/menulogo2.jpg")
        self.MenuLogo2=self.MenuLogo2.resize((185,185),Image.ANTIALIAS)
        self.MenuLogo2=ImageTk.PhotoImage(self.MenuLogo2)
        lbl_menulogo=Label(LeftMenu, image=self.MenuLogo2)
        lbl_menulogo.pack(side=TOP, fill=X)

        self.lbl_albumnumber=Label(self.root,text="Total Albums\n14",bd=5,relief=RIDGE,bg="#fcb293",fg="white",font=("courier new",20,"bold"))
        self.lbl_albumnumber.place(x=275,y=150,height=150,width=300)

        self.lbl_artistnumber=Label(self.root,text="Total Artists\n4",bd=5,relief=RIDGE,bg="#fcb293",fg="white",font=("courier new",20,"bold"))
        self.lbl_artistnumber.place(x=625,y=325,height=150,width=300)

        self.lbl_songnumber=Label(self.root,text="Total Songs\n14",bd=5,relief=RIDGE,bg="#fcb293",fg="white",font=("courier new",20,"bold"))
        self.lbl_songnumber.place(x=975,y=500,height=150,width=300)

    def record(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=recordclass(self.new_win)

    def newartist(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=newartistclass(self.new_win)

    def about(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=aboutclass(self.new_win)

if __name__=="__main__":
    root=Tk()
    obj=Melody(root)
    root.mainloop()