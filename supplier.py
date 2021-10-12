from sqlite3.dbapi2 import Cursor, connect
from tkinter import *  
from PIL import ImageTk
import PIL.Image
from tkinter import ttk, messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1055x485+205+127")
        self.root.title("Supplier | IMS | Developed by Amit")
        self.root.config(bg="white")
        photo = PhotoImage(file = "images\i1.png")
        self.root.iconphoto(False, photo)
        self.root.focus_force()
        self.root.resizable(False, False)
        #root.overrideredirect(1)

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        #All variables

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()



        #-----Search-----
        #====Options====
        lbl_search = Label(self.root, text="Invoice No.",  bg="white",font=("goudy old style", 15))
        lbl_search.place(x=690, y=80, width=88)

        txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="azure2")
        txt_search.place(x=785,y=80, width=165)

        btn_search = Button(self.root, command=self.search, cursor="hand2", text="Search", font=("goudy old style", 15), bg="purple4", fg="white")
        btn_search.place(x=955,y=79,width=90, height=27)

        #---Title---
        title = Label(self.root, text="Supplier Details", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white").place(x=50,y=10,width=955, height=40)

        #---Contant----
        #---Row1---

        lbl_supplier_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white").place(x=50,y=80)
        txt__supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg ="azure2").place(x=180,y=80, width=180)

        #---Row2---

        lbl_name = Label(self.root, text="Supplier Name", font=("goudy old style", 15), bg="white").place(x=50,y=120)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg ="azure2").place(x=180,y=120, width=180)
        #====Row3====

        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=50,y=160)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg ="azure2").place(x=180,y=160, width=180)
        #===Row4===

        lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15), bg="white").place(x=50,y=200)
        self.txt_desc = Text(self.root, font=("goudy old style", 15), bg ="azure2")
        self.txt_desc.place(x=180,y=200, width=470, height=120)
        #----Button---
        btn_add = Button(self.root, command=self.add, cursor="hand2", text="Save", font=("goudy old style", 15), bg="SeaGreen2", fg="white").place(x=150,y=350,width=98, height=35)

        btn_update = Button(self.root, command=self.update, cursor="hand2", text="Update", font=("goudy old style", 15), bg="cadet blue", fg="white").place(x=255,y=350,width=98, height=35)

        btn_delete = Button(self.root, command=self.delete, cursor="hand2", text="Delete", font=("goudy old style", 15), bg="goldenrod", fg="white").place(x=360,y=350,width=98, height=35)

        btn_clear = Button(self.root, command=self.clear,cursor="hand2", text="Clear", font=("goudy old style", 15), bg="SlateGray2", fg="white").place(x=465,y=350,width=98, height=35)

        btn_exit = Button(self.root, cursor="hand2", text="Exit", font=("goudy old style", 15), command=self.exit, bg="red", fg="white").place(x=570,y=350,width=98, height=35)


        #===Supplier details===

        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=690,y=120,width=355, height=350)

        scrolly = Scrollbar(emp_frame, orient= VERTICAL)
        scrollx = Scrollbar(emp_frame, orient= HORIZONTAL)



        self.SupplierTable = ttk.Treeview(emp_frame, columns=("invoice", "name", "contact", "desc"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice", text="Invoice")
        self.SupplierTable.heading("name", text="Supplier Name")
        self.SupplierTable.heading("contact", text="Contact")
        self.SupplierTable.heading("desc", text="Description")
        self.SupplierTable["show"] = "headings"

        self.SupplierTable.column("invoice", width=90)
        self.SupplierTable.column("name", width=100)
        self.SupplierTable.column("contact", width=100)
        self.SupplierTable.column("desc", width=100)
        self.SupplierTable.pack(expand=1, fill=BOTH)
        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()


##########################################################################################################################################
##########################################################################################################################################

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Invoice no. already assigned, try different", parent=self.root)
                else:
                    cur.execute("Insert into supplier(invoice, name, contact, desc) values(?,?,?,?)", (
                                        self.var_sup_invoice.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_desc.get('1.0', END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])

        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END,row[3])

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice no. must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice no.", parent=self.root)
                else:
                    cur.execute("Update supplier set name=?, contact=?, desc=? where  invoice=?", (
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_desc.get('1.0', END),
                                        self.var_sup_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice no. must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice no.", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Supplier Deleted Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":   
                messagebox.showerror("Error", "Invoice no. should be required", parent=self.root)

            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error", "No record found.", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)



    def exit(self):
        self.root.destroy()

if __name__ =="__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()