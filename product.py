from sqlite3.dbapi2 import Cursor, connect
from tkinter import *
from tkinter.font import BOLD  
from PIL import ImageTk
import PIL.Image
from tkinter import ttk, messagebox
import sqlite3

class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1055x485+205+127")
        self.root.title("Product | IMS | Developed by Amit")
        self.root.config(bg="white")
        photo = PhotoImage(file = "images\i1.png")
        self.root.iconphoto(False, photo)
        self.root.focus_force()
        self.root.resizable(False, False)
        #root.overrideredirect(1)

        #########################################

        self.var_pid =StringVar()
        self.var_cat =StringVar()
        self.var_sup =StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()

        self.var_name =StringVar()
        self.var_price =StringVar()
        self.var_qty =StringVar()
        self.var_status =StringVar()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()


        #---Frame---
        product_Frame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        product_Frame.place(x=10,y=10,width=450,height=465)
        
        #---Title--
        title = Label(product_Frame, text="Manage Product Details", font=("goudy old style", 15, "bold"), bg="IndianRed4", fg="white").pack(side=TOP,fill=X)

        #---colum1---
        lbl_category = Label(product_Frame, text="Category", font=("goudy old style", 15), bg="white").place(x=30,y=60)
        lbl_supplier = Label(product_Frame, text="Supplier", font=("goudy old style", 15), bg="white").place(x=30,y=110)
        lbl_product = Label(product_Frame, text="Name", font=("goudy old style", 15), bg="white").place(x=30,y=160)
        lbl_price = Label(product_Frame, text="Price", font=("goudy old style", 15), bg="white").place(x=30,y=210)
        lbl_qty = Label(product_Frame, text="Quantity", font=("goudy old style", 15), bg="white").place(x=30,y=260)
        lbl_status = Label(product_Frame, text="Status", font=("goudy old style", 15), bg="white").place(x=30,y=310)

        #---colum2---

        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.cat_list, state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_cat.place(x=150, y=60, width=200)
        cmb_cat.current(0)

        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=self.sup_list, state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_sup.place(x=150, y=110, width=200)
        cmb_sup.current(0)

        #--------

        txt_name = Entry(product_Frame, textvariable=self.var_name, font=("goudy old style", 15), bg="azure2")
        txt_name.place(x=150, y=160, width=200)

        txt_price = Entry(product_Frame, textvariable=self.var_price, font=("goudy old style", 15), bg="azure2")
        txt_price.place(x=150, y=210, width=200)

        txt_qty = Entry(product_Frame, textvariable=self.var_qty, font=("goudy old style", 15), bg="azure2")
        txt_qty.place(x=150, y=260, width=200) 

        #-----
        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Active", "Inactive"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_status.place(x=150, y=310, width=200)
        cmb_status.current(0)   

        #---Button--
        btn_add = Button(product_Frame, command=self.add, cursor="hand2", text="Save", font=("goudy old style", 15), bg="cyan4", fg="white").place(x=9,y=400,width=100, height=40)

        btn_update = Button(product_Frame, command=self.update, cursor="hand2", text="Update", font=("goudy old style", 15), bg="green3", fg="white").place(x=118,y=400,width=100, height=40)

        btn_delete = Button(product_Frame, command=self.delete, cursor="hand2", text="Delete", font=("goudy old style", 15), bg="red2", fg="white").place(x=227,y=400,width=100, height=40)

        btn_clear = Button(product_Frame, command=self.clear,cursor="hand2", text="Clear", font=("goudy old style", 15), bg="khaki3", fg="white").place(x=336,y=400,width=100, height=40)


        #---Search---
        SearchFrame=LabelFrame(self.root, text="Search Employee", bg="white", font=("goudy old style",12,"bold"))
        SearchFrame.place(x=470, y=10,width=580,height=80)

        #====Options====
        cms_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Category", "Supplier", "Name"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cms_search.place(x=10, y=10, width=180)
        cms_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="azure2")
        txt_search.place(x=200,y=10, height=30)

        btn_search = Button(SearchFrame, command=self.search, cursor="hand2", text="Search", font=("goudy old style", 15), bg="dark sea green", fg="white")
        btn_search.place(x=410,y=9,width=150, height=30)

        #===Product details===

        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=470,y=100,width=575, height=374)

        scrolly = Scrollbar(p_frame, orient= VERTICAL)
        scrollx = Scrollbar(p_frame, orient= HORIZONTAL)



        self.product_table = ttk.Treeview(p_frame, columns=("pid", "Category", "Supplier", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("pid", text="Product ID")    
        self.product_table.heading("Category", text="Category") 
        self.product_table.heading("Supplier", text="Supplier")  
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Quantity")
        self.product_table.heading("status", text="Status")
        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=90)
        self.product_table.column("Category", width=100)
        self.product_table.column("Supplier", width=100)        
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=100)
        self.product_table.column("qty", width=100)
        self.product_table.column("status", width=100)
        self.product_table.pack(expand=1, fill=BOTH)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)

        self.show()



##########################################################################################################################################
##########################################################################################################################################

    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")        
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select name from category")
            cat=cur.fetchall()

            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("Select name from supplier")
            sup=cur.fetchall()

            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get() =="Select" or self.var_sup.get()=="Empty" or self.var_name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product already present, try different", parent=self.root)
                else:
                    cur.execute("Insert into product(Category, Supplier, name, price, qty, status) values(?,?,?,?,?,?)", (
                                        self.var_cat.get(),
                                        self.var_sup.get(),                                        
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),

                                        self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Added Successfully", parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])        
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
 

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error", "Please select product from list", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product", parent=self.root)
                else:
                    cur.execute("Update product set Category=?, Supplier=?, name=?, price=?, qty=?, status=? where  pid=?", (
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_status.get(),
                                        self.var_pid.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error", "Select product from the list", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Product Deleted Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_sup.set("Select"),
        self.var_cat.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Active"),
        self.var_pid.set("")

        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error", "Select search by option", parent=self.root)

            elif self.var_searchtxt.get()=="":   
                messagebox.showerror("Error", "Select input should be required", parent=self.root)

            else:
                cur.execute("Select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)

                else:
                    messagebox.showerror("Error", "No record found.", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)




if __name__ =="__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()