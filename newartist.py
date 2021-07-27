from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class newartistclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1110x555+220+140")
        self.root.title("Add New Artist")
        self.root.config(bg="#e0cee0")
        self.root.focus_force()

        self.var_artistid=StringVar()
        self.var_artistname=StringVar()
        self.var_artistage=StringVar()
        self.var_artistgender=StringVar()
        self.var_artistcountry=StringVar()

        lbl_title=Label(self.root,text="Add a new artist by filling in the details below",font=("cambria",25,"bold"),bg="#a37e7e",fg="#d3ccca").pack(side=TOP,fill=X,padx=75,pady=15)

        lbl_name=Label(self.root,text="Enter Artist Name:",font=("courier new",17,"bold"),bg="#e0cee0",fg="black")
        lbl_name.place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_artistname,font=("courier new",15,"bold"),bg="white",fg="black").place(x=375,y=100,width=450,height=30)

        lbl_age=Label(self.root,text="Enter Artist Age:",font=("courier new",17,"bold"),bg="#e0cee0",fg="black")
        lbl_age.place(x=50,y=175)
        txt_age=Entry(self.root,textvariable=self.var_artistage,font=("courier new",15,"bold"),bg="white",fg="black").place(x=375,y=175,width=450,height=30)

        lbl_gender=Label(self.root,text="Enter Artist Gender:",font=("courier new",17,"bold"),bg="#e0cee0",fg="black")
        lbl_gender.place(x=50,y=250)
        txt_gender=Entry(self.root,textvariable=self.var_artistgender,font=("courier new",15,"bold"),bg="white",fg="black").place(x=375,y=250,width=450,height=30)
        lbl_extra=Label(self.root,text="(Male/Female/Other)",font=("courier new",14),bg="#e0cee0",fg="grey")
        lbl_extra.place(x=850,y=250)

        lbl_country=Label(self.root,text="Enter Artist Country:",font=("courier new",17,"bold"),bg="#e0cee0",fg="black")
        lbl_country.place(x=50,y=325)
        txt_country=Entry(self.root,textvariable=self.var_artistcountry,font=("courier new",15,"bold"),bg="white",fg="black").place(x=375,y=325,width=450,height=30)
        
        btn_add=Button(self.root,text='Add',command=self.add,font=("courier new",17,"bold"),bg="#77dd76",fg="black",cursor="hand2").place(x=375,y=450,width=150,height=30)
        btn_delete=Button(self.root,text='Clear',command=self.clear,font=("courier new",17,"bold"),bg="#ff6962",fg="black",cursor="hand2").place(x=675,y=450,width=150,height=30)

    def add(self):
        con=sqlite3.connect(database=r'melody.db')
        cur=con.cursor()
        try:
            cur.execute("Insert into artists (name,age,gender,country) values(?,?,?,?)",(
                self.var_artistname.get(),
                self.var_artistage.get(),
                self.var_artistgender.get(),
                self.var_artistcountry.get(),
            ))
            con.commit()
            messagebox.showinfo("Success","Record has been added succesfully!",parent=self.root)
            self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")
    
    def clear(self):
        self.var_artistname.set("")
        self.var_artistage.set("")
        self.var_artistgender.set("")
        self.var_artistcountry.set("")

if __name__=="__main__":
    root=Tk()
    obj=newartistclass(root)
    root.mainloop()