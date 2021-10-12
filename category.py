from sqlite3.dbapi2 import Cursor, connect
from tkinter import *
from tkinter.font import BOLD  
from PIL import ImageTk
import PIL.Image
from tkinter import ttk, messagebox
import sqlite3

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1055x485+205+127")
        self.root.title("Category | IMS | Developed by Amit")
        self.root.config(bg="white")
        photo = PhotoImage(file = "images\i1.png")
        self.root.iconphoto(False, photo)
        self.root.focus_force()
        self.root.resizable(False, False)
        #root.overrideredirect(1)

        #============Variables===========

        self.var_cat_id=StringVar()
        self.var_name=StringVar()

        #=====tittle====
        title = Label(self.root, text="Manage Product Category", font=("goudy old style", 20, "bold"), bg="#184a45", fg="white", bd=5,relief=RIDGE).pack(side=TOP, fill=X, padx=10,pady=10)

        lbl_name = Label(self.root, text="Enter Category Name", font=("goudy old style", 20, "bold"), bg="white").place(x=50,y=100)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 18), bg="azure2").place(x=50,y=170, width=300)
        
        btn_add = Button(self.root, command=self.add, text="Add", font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=360,y=169, width=150, height=30)
        btn_delete = Button(self.root, command=self.delete, text="Delete", font=("goudy old style", 15), bg="red", fg="white", cursor="hand2").place(x=520,y=169, width=150, height=30)


         #===Category details===

        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=690,y=100,width=355, height=100)

        scrolly = Scrollbar(cat_frame, orient= VERTICAL)
        scrollx = Scrollbar(cat_frame, orient= HORIZONTAL)



        self.CategoryTable = ttk.Treeview(cat_frame, columns=("cid", "name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)

        self.CategoryTable.heading("cid", text="Category ID")
        self.CategoryTable.heading("name", text="Name")
        self.CategoryTable["show"] = "headings"

        self.CategoryTable.column("cid", width=90)
        self.CategoryTable.column("name", width=100)
        self.CategoryTable.pack(expand=1, fill=BOTH)
        self.CategoryTable.bind("<ButtonRelease-1>", self.get_data)

        #====Images====
        self.im1= PIL.Image.open("images/cat1.png")
        self.im1=self.im1.resize((490,240),PIL.Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1 = Label(self.root, image=self.im1, bd=1,relief=RAISED, bg="white")
        self.lbl_im1.place(x=25, y=220)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.im2= PIL.Image.open("images/cat2.png")
        self.im2=self.im2.resize((490,240),PIL.Image.ANTIALIAS)
        self.im2=ImageTk.PhotoImage(self.im2)

        self.lbl_im2 = Label(self.root, image=self.im2, bd=1,relief=RAISED, bg="white")
        self.lbl_im2.place(x=535, y=220)

        self.show()
    ######################Function############################
      
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error", "Category name should be required", parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Category already present, try different", parent=self.root)
                else:
                    cur.execute("Insert into category(name) values(?)", (self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
                    self.show()
                    self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f=self.CategoryTable.focus()
        content=(self.CategoryTable.item(f))
        row=content['values']

        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error", "Please select category from the list", parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error, Please try again", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Category Deleted Successfully", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ =="__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()