from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class recordclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1110x555+220+140")
        self.root.title("All Records")
        self.root.config(bg="#e0cee0")
        self.root.focus_force()

        self.var_searchby=StringVar()
        self.var_searchtext=StringVar()
        
        self.var_id=StringVar()
        self.var_song=StringVar()
        self.var_album=StringVar()
        self.var_artist=StringVar()
        self.var_year=StringVar()
        self.var_genre=StringVar()

        SearchFrame=LabelFrame(self.root,text="Search Records",font=("cambria",15,"bold"),bd=2,relief=RIDGE,bg="#e0cee0")
        SearchFrame.place(x=250,y=20,width=585,height=70)
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Song Name","Album Name","Artist Name"),font=("courier new",12,"bold"),state='readonly',justify=CENTER)
        cmb_search.place(x=10,y=10,width=180, height=25)
        cmb_search.current(0)
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtext,font=("courier new",12,"bold"),bg="white").place(x=200, y=10, width=180, height=25)
        btn_search=Button(SearchFrame,text='Search',command=self.search,font=("courier new",12,"bold"),bg="#77dd76",fg="black",cursor="hand2").place(x=390,y=10,width=180,height=25)

        title=Label(self.root,text="Record Details",font=("cambria",15,"bold"),bg="#bc85a3",fg="white").place(x=50,y=100,width=1000)

        lbl_id=Label(self.root,text="ID:",font=("courier new",12,"bold"),bg="#e0cee0").place(x=50,y=150)
        lbl_song=Label(self.root,text="Song Name:",font=("courier new",12,"bold"),bg="#e0cee0").place(x=175,y=150)
        lbl_album=Label(self.root,text="Album Name:",font=("courier new",12,"bold"),bg="#e0cee0").place(x=625,y=150)

        txt_id=Entry(self.root,textvariable=self.var_id,font=("courier new",12,"bold"),bg="white").place(x=100,y=150,width=50)
        txt_song=Entry(self.root,textvariable=self.var_song,font=("courier new",12,"bold"),bg="white").place(x=325,y=150,width=275)
        txt_album=Entry(self.root,textvariable=self.var_album,font=("courier new",12,"bold"),bg="white").place(x=775,y=150,width=275)

        lbl_artist=Label(self.root,text="Artist:",font=("courier new",12,"bold"),bg="#e0cee0").place(x=50,y=200)
        lbl_year=Label(self.root,text="Year of Release:",font=("courier new",12,"bold"),bg="#e0cee0").place(x=435,y=200)
        lbl_genre=Label(self.root,text="Genre:",font=("courier new",12,"bold"),bg="#e0cee0").place(x=765,y=200)

        txt_artist=Entry(self.root,textvariable=self.var_artist,font=("courier new",12,"bold"),bg="white").place(x=150,y=200,width=225)
        txt_year=Entry(self.root,textvariable=self.var_year,font=("courier new",12,"bold"),bg="white").place(x=625,y=200,width=100)
        txt_genre=Entry(self.root,textvariable=self.var_genre,font=("courier new",12,"bold"),bg="white").place(x=850,y=200,width=200)

        btn_save=Button(self.root,text='Save',command=self.add,font=("courier new",12,"bold"),bg="#89cff0",fg="black",cursor="hand2").place(x=50,y=250,width=180,height=25)
        btn_update=Button(self.root,text='Update',command=self.update,font=("courier new",12,"bold"),bg="#77dd76",fg="black",cursor="hand2").place(x=325,y=250,width=180,height=25)
        btn_delete=Button(self.root,text='Delete',command=self.delete,font=("courier new",12,"bold"),bg="#ff6962",fg="black",cursor="hand2").place(x=600,y=250,width=180,height=25)
        btn_clear=Button(self.root,text='Clear',command=self.clear,font=("courier new",12,"bold"),bg="#cfcfc4",fg="black",cursor="hand2").place(x=875,y=250,width=180,height=25)

        table_frame=Frame(self.root,bd=3,relief=RIDGE)
        table_frame.place(x=10,y=300,relwidth=0.98,height=250)

        scrolly=Scrollbar(table_frame,orient=VERTICAL)
        scrollx=Scrollbar(table_frame,orient=HORIZONTAL)

        self.Table=ttk.Treeview(table_frame,columns=("id","song","album","artist","year","genre"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Table.xview)
        scrolly.config(command=self.Table.yview)

        self.Table.heading("id",text="ID")
        self.Table.heading("song",text="Song Name")
        self.Table.heading("album",text="Album Name")
        self.Table.heading("artist",text="Artist")
        self.Table.heading("year",text="Year of Release")
        self.Table.heading("genre",text="Genre")

        self.Table["show"]="headings"

        self.Table.column("id",width=25)
        self.Table.column("song",width=200)
        self.Table.column("album",width=200)
        self.Table.column("artist",width=200)
        self.Table.column("year",width=50)
        self.Table.column("genre",width=100)
        self.Table.pack(fill=BOTH,expand=1)
        self.Table.bind("<ButtonRelease-1>",self.get_data)

        self.show()

    def add(self):
        con=sqlite3.connect(database=r'melody.db')
        cur=con.cursor()
        try:
            if self.var_id.get()=="":
                messagebox.showerror("Error","ID must be entered",parent=self.root)
            else:
                cur.execute("Select * from records where id=?",(self.var_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This ID already exists, try with a different number!")
                else:
                    cur.execute("Insert into records (id,song,album,artist,year,genre) values(?,?,?,?,?,?)",(
                        self.var_id.get(),
                        self.var_song.get(),
                        self.var_album.get(),
                        self.var_artist.get(),
                        self.var_year.get(),
                        self.var_genre.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Record has been added succesfully!",parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def show(self):
        con=sqlite3.connect(database=r'melody.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from records")
            rows=cur.fetchall()
            self.Table.delete(*self.Table.get_children())
            for row in rows:
                self.Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def get_data(self,ev):
        f=self.Table.focus()
        content=(self.Table.item(f))
        row=content['values']
        self.var_id.set(row[0])
        self.var_song.set(row[1])
        self.var_album.set(row[2])
        self.var_artist.set(row[3])
        self.var_year.set(row[4])
        self.var_genre.set(row[5])

    def update(self):
        con=sqlite3.connect(database=r'melody.db')
        cur=con.cursor()
        try:
            if self.var_id.get()=="":
                messagebox.showerror("Error","ID must be entered",parent=self.root)
            else:
                cur.execute("Select * from records where id=?",(self.var_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID. Please try again!")
                else:
                    cur.execute("Update records set song=?,album=?,artist=?,year=?,genre=? where id=?",(
                        self.var_song.get(),
                        self.var_album.get(),
                        self.var_artist.get(),
                        self.var_year.get(),
                        self.var_genre.get(),
                        self.var_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Record has been updated succesfully!",parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def delete(self):
        con=sqlite3.connect(database=r'melody.db')
        cur=con.cursor()
        try:
            if self.var_id.get()=="":
                messagebox.showerror("Error","ID must be entered",parent=self.root)
            else:
                cur.execute("Select * from records where id=?",(self.var_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID. Please try again!")
                else:
                    op=messagebox.askyesno("Confirm","Are you sure you want to delete record?",parent=self.root)
                    if op==True:
                        cur.execute("delete from records where id=?",(self.var_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Record deleted successfully!",parent=self.root)
                        self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

    def clear(self):
        self.var_id.set("")
        self.var_song.set("")
        self.var_album.set("")
        self.var_artist.set("")
        self.var_year.set("")
        self.var_genre.set("")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'melody.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="":
                messagebox.showerror("Error","Select search type!",parent=self.root)
            elif self.var_searchtext.get()=="":
                messagebox.showerror("Error","Search text required!",parent=self.root)
            else:
                cur.execute("Select * from records where"+self.var_searchby.get()+" LIKE '%"+self.var_searchtext.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.Table.delete(*self.Table.get_children())
                    for row in rows:
                        self.Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No records found!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=recordclass(root)
    root.mainloop()