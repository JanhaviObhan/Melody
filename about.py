from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import webbrowser

def callback(url):
    webbrowser.open_new(url)

class aboutclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1110x555+220+140")
        self.root.title("About")
        self.root.config(bg="#e0cee0")
        self.root.focus_force()

        self.lbl_albumnumber=Label(self.root,text="About The System",bd=5,relief=RIDGE,bg="#ffcbc1",fg="grey",font=("courier new",18,"bold"))
        self.lbl_albumnumber.place(x=75,y=50,height=75,width=300)

        self.lbl_albumnumber=Label(self.root,text="The Music Album Management system is made as a course\nassignment for Python course studied in Semester IV of\nEngineering in Information Technology. The aim was to learn\nand implement a GUI for practical use using Python\nenvironment. This project was guided by Mrs. Sarita Rathod,\nAssistant Professor at K.J. Somaiya Institute\nof Engineering and Information Technology.",bd=5,relief=RIDGE,bg="#f3ffe3",fg="black",font=("courier new",13,"bold"))
        self.lbl_albumnumber.place(x=450,y=50,height=200,width=610)

        self.lbl_artistnumber=Label(self.root,text="Contact The Creator",bd=5,relief=RIDGE,bg="#ffcbc1",fg="grey",font=("courier new",18,"bold"))
        self.lbl_artistnumber.place(x=75,y=300,height=75,width=300)

        self.lbl_albumnumber=Label(self.root,text="For any queries:\nEmail: janhavi.obhan@somaiya.edu\nContact Number: 9322935775\nInstagram:            ",bd=5,relief=RIDGE,bg="#f3ffe3",fg="black",font=("courier new",15,"bold"))
        self.lbl_albumnumber.place(x=450,y=300,height=200,width=610)

        self.link1 = Label(root, text="@jjaann2809", bg="#f3ffe3", fg="blue", cursor="hand2",font=("courier new",15,"bold"))
        self.link1.pack()
        self.link1.bind("<Button-1>", lambda e: callback("https://www.instagram.com/jjaann2809/"))
        self.link1.place(x=750,y=420)

if __name__=="__main__":
    root=Tk()
    obj=aboutclass(root)
    root.mainloop()